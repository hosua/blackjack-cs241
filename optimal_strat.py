from card_engine import *
from card_handler import *
from matplotlib import pyplot as plt
import numpy as np
import json
from datetime import datetime
import os
import re
import sys

SAVE_DIR = 'data'

"""
THIS IS OUR CONTROL, running this script will give us the data of the expected outcome when
following the optimal strategy depicted by this chart: https://www.kjartan.co.uk/games/pix/cards/Blackjack%20full%20guide.pdf
in a standard, unmodified game of Blackjack
"""

# strategy dict involving player hands with no aces
# key = known_dealer_score, value = player hit range (start, end) inclusive
hard_hands = {
        1: (4,17), # Dealer has ace
        2: (4,12),
        3: (4,12),
        4: (4,11),
        5: (4,11),
        6: (4,11),
        7: (4,16),
        8: (4,16),
        9: (4,16),
        10: (4,16),
        11: (4,17), # Dealer has ace
        }

# strategy dict involving player hands with aces
# key = known_dealer_score, value = player hit range (start, end) inclusive
soft_hands = {
        1: (12,18), # Dealer has ace
        2: (12,18), 
        3: (12,18), 
        4: (12,18), 
        5: (12,18), 
        6: (12,18), 
        7: (12,17), 
        8: (12,17), 
        9: (12,18), 
        10: (12,18), 
        11: (12,18), # Dealer has ace
        }

# Returns true or false depending on if the player should hit according to the optimal strategy
# The flag is_hard is true if the player has no aces in their hand
def decision_maker(player_score: int, known_dealer_score: int, is_hard: int) -> bool:
    if is_hard:
        # print("HARD HAND")
        hit_list = list(range(hard_hands[known_dealer_score][0], hard_hands[known_dealer_score][1]+1))
        # print(f"Player should hit if score is in: {hit_list}")
        if player_score in hit_list:
            return True
    else:
        # print("SOFT HAND")
        hit_list = list(range(soft_hands[known_dealer_score][0], soft_hands[known_dealer_score][1]+1))
        # print(f"Player should hit if score is in: {hit_list}")
        if player_score in hit_list:
            return True
    return False

def optimal_play():
    # Creates deck for game
    deck = Deck("Blackjack")

    player = Hand()
    dealer = Hand()

    # Tests
    # ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
    # frequencies = [4] * 9
    # card_types = dict(zip(ranks, frequencies))
    # if card_types:
    #     deck.remove_from_deck(card_types)

    dealer_start(dealer, deck)
    player_start(player, deck)

    known_dealer_score = value(dealer)

    while True:
        is_hard = check_hard(player)
        if total_value(player) == 21:
            dealer_open(dealer)
            if total_value(dealer) != 21:
                if not HIDE_OUTPUT: 
                    print("Blackjack! Player wins!\n")
                return 2
            else:
                if not HIDE_OUTPUT: 
                    print("Tie!\n")
                return 1
        if decision_maker(total_value(player), known_dealer_score, is_hard):
            if not HIDE_OUTPUT:
                print("PLAYER HIT")
            p_hit(player, deck)
            if total_value(player) == 21:
                dealer_open(dealer)
                if total_value(dealer) == 21:
                    if not HIDE_OUTPUT: 
                        print("Tie!\n")
                    return 1
                else:
                    if not HIDE_OUTPUT: 
                        print("Blackjack! Player wins!\n")
                    return 2
            elif total_value(player) > 21:
                if not HIDE_OUTPUT: 
                    print("Player bust! Player loses!\n")
                return 0
        else:
            if not HIDE_OUTPUT:
                print("PLAYER STAND")
            if total_value(dealer) < 17:
                while total_value(dealer) < 17:
                    d_hit(dealer, deck)

                if total_value(dealer) == total_value(player):
                    if not HIDE_OUTPUT: 
                        print("Tie!\n")
                    return 1
                elif total_value(dealer) == 21:
                    if not HIDE_OUTPUT: 
                        print("Player loses!\n")
                    return 0
                elif total_value(dealer) > 21:
                    if not HIDE_OUTPUT: 
                        print("Dealer bust! Player wins!\n")
                    return 2
                elif total_value(dealer) > total_value(player):
                    if not HIDE_OUTPUT: 
                        print("Player loses!\n")
                    return 0
                else:
                    if not HIDE_OUTPUT: 
                        print("Player wins!\n")
                    return 2
            else:
                dealer_open(dealer)
                if total_value(dealer) == total_value(player):
                    if not HIDE_OUTPUT: 
                        print("Tie!\n")
                    return 1
                if total_value(dealer) == 21:
                    if not HIDE_OUTPUT: 
                        print("Player loses!\n")
                    return 0
                if total_value(dealer) > 21:
                    if not HIDE_OUTPUT: 
                        print("Dealer bust! Player wins!\n")
                    return 2
                if total_value(dealer) > total_value(player):
                    if not HIDE_OUTPUT: 
                        print("Player loses!\n")
                    return 0
                else:
                    if not HIDE_OUTPUT: 
                        print("Player wins!\n")
                    return 2

def run_optimal(trials: int) -> dict:
    stats_dict: dict
    thresh_min: int
    thresh_max: int
    res: int # 0 -> lose, 1 -> draw, 2 -> win

    stats_dict = {'lose': 0, 'draw': 0, 'win': 0}
    thresh_min, thresh_max = 2, 20
    for trial in range(trials):
        if (trial % 10000 == 0):
            print(trial)
        res = optimal_play()
        if res == 0:
            stats_dict['lose'] += 1
        elif res == 1:
            stats_dict['draw'] += 1
        elif res == 2:
            stats_dict['win'] += 1

    print(stats_dict)
    return stats_dict

""" Returns plt object """
def graph_data(trials: int, stats_dict: dict, fname: str) -> plt:
    y_ticks: int
    if trials > 10:
        y_ticks = range(0, trials, trials//10)
    else:
        y_ticks = range(0, 10)

    fig, ax = plt.subplots()
    statuses = ['losses', 'draws', 'wins']
    freqs = [stats_dict['lose'], stats_dict['draw'], stats_dict['win']]

    ax.bar(statuses, freqs)
    plt.title(f"Optimal Vanilla Strategy")
    ax.set_xticklabels(('losses', 'draws', 'wins'))
    output_fname = f"{SAVE_DIR}/{fname}"
    plt.savefig(output_fname)
    print(f"Saved graph to {output_fname}")
    return plt

""" Dump stats_dict into json file """
def dump_json(stats_dict: dict, path_prefix: str):

    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)

    output_fname = f"{SAVE_DIR}/{path_prefix}"

    with open(output_fname, "w") as f:
        json.dump(stats_dict, f, indent=2)
    print(f"Dumped data to {output_fname}")

""" Returns the next available filename given a prefix and extension """
def get_next_name(path_prefix: str, ext: str) -> str:
    i: int = 0
    os.chdir(SAVE_DIR)
    prefix_pattern = f"^{path_prefix}-(.*)"
    ext_pattern = f".*{ext}$"
    extract_number_pattern = "T\d+-"
    for f in sorted(os.listdir()):
        root, f_ext = os.path.splitext(os.path.expanduser(f))
        fname = os.path.basename(root)
        if re.match(prefix_pattern, root) and re.match(ext_pattern, f_ext):
            f_num = int(re.match(prefix_pattern, root).group(1))
            i = f_num+1

    os.chdir("..")
    return f"{path_prefix}-{str(i).zfill(4)}.{ext}"

DATA_FNAME = "optimal-vanilla"
if __name__ == "__main__":
    trials = 1000000
    
    if len(sys.argv) > 1:
        try:
            trials = int(sys.argv[1])
        except ValueError:
            print("Error: Argument must be an integer")
            exit(1)

    stats_dict = run_optimal(trials)

    # get next available file name
    json_fname = get_next_name(DATA_FNAME, "json")
    plt_fname = get_next_name(DATA_FNAME, "png")

    graph_plt = graph_data(trials, stats_dict, plt_fname)

    dump_json(stats_dict, json_fname)
    # graph_plt.show()

    # h = Hand([Card('Clubs', 'Ace'), Card('Clubs', 'Ace'), Card('Clubs', 'Ace')])
    # h = Hand([Card('Clubs', 'Ace'), Card('Clubs', 'Ace')])
    # print(h.show_info())
    # print(total_value(h))
