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
To prevent any confusion, this is NOT the optimal strategy for our modified deck. This is simply just running the
same strategy used on a standard deck, against a deck with no face cards.
This script will run the same exact strategy used in optimal_strat.py against a modified deck
of cards containing no face cards in the deck. 
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

# Note that this isn't an "optimal strat" for the given deck, this is using the same optimal strategy
# from a normal deck to check if the results change for better or for worse. (It changes for worse, thank god
# my code works)
def optimal_strat_nofaces():
    # Creates deck for game
    deck = Deck("Blackjack", removed=True)

    player = Hand()
    dealer = Hand()

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
                return 2, dealer.hand[0].get_rank()
            else:
                if not HIDE_OUTPUT: 
                    print("Tie!\n")
                return 1, dealer.hand[0].get_rank()
        if decision_maker(total_value(player), known_dealer_score, is_hard):
            if not HIDE_OUTPUT:
                print("PLAYER HIT")
            p_hit(player, deck)
            if total_value(player) == 21:
                dealer_open(dealer)
                if total_value(dealer) == 21:
                    if not HIDE_OUTPUT: 
                        print("Tie!\n")
                    return 1, dealer.hand[0].get_rank()
                else:
                    if not HIDE_OUTPUT: 
                        print("Blackjack! Player wins!\n")
                    return 2, dealer.hand[0].get_rank()
            elif total_value(player) > 21:
                if not HIDE_OUTPUT: 
                    print("Player bust! Player loses!\n")
                return 0, dealer.hand[0].get_rank()
        else:
            if not HIDE_OUTPUT:
                print("PLAYER STAND")
            if total_value(dealer) < 17:
                while total_value(dealer) < 17:
                    d_hit(dealer, deck)

                if total_value(dealer) == total_value(player):
                    if not HIDE_OUTPUT: 
                        print("Tie!\n")
                    return 1, dealer.hand[0].get_rank()
                elif total_value(dealer) == 21:
                    if not HIDE_OUTPUT: 
                        print("Player loses!\n")
                    return 0, dealer.hand[0].get_rank()
                elif total_value(dealer) > 21:
                    if not HIDE_OUTPUT: 
                        print("Dealer bust! Player wins!\n")
                    return 4, dealer.hand[0].get_rank()
                elif total_value(dealer) > total_value(player):
                    if not HIDE_OUTPUT: 
                        print("Player loses!\n")
                    return 0, dealer.hand[0].get_rank()
                else:
                    if not HIDE_OUTPUT: 
                        print("Player wins!\n")
                    return 2, dealer.hand[0].get_rank()
            else:
                dealer_open(dealer)
                if total_value(dealer) == total_value(player):
                    if not HIDE_OUTPUT: 
                        print("Tie!\n")
                    return 1, dealer.hand[0].get_rank()
                if total_value(dealer) == 21:
                    if not HIDE_OUTPUT: 
                        print("Player loses!\n")
                    return 0, dealer.hand[0].get_rank()
                if total_value(dealer) > 21:
                    if not HIDE_OUTPUT: 
                        print("Dealer bust! Player wins!\n")
                    return 4, dealer.hand[0].get_rank()
                if total_value(dealer) > total_value(player):
                    if not HIDE_OUTPUT: 
                        print("Player loses!\n")
                    return 0, dealer.hand[0].get_rank()
                else:
                    if not HIDE_OUTPUT: 
                        print("Player wins!\n")
                    return 2, dealer.hand[0].get_rank()

def run_optimal(trials: int) -> dict:
    stats_dict: dict
    res: int # 0 -> lose, 1 -> draw, 2 -> win

    stats_dict = {'lose': 0, 'draw': 0, 'win': 0, 'dealer_bust': [], 'dealer_card_freqs': []}
    for trial in range(trials):
        if (trial % 10000 == 0):
            print(trial)
        res = optimal_strat_nofaces()
        if res[0] == 0:
            stats_dict['lose'] += 1
        elif res[0] == 1:
            stats_dict['draw'] += 1
        elif res[0] == 2:
            stats_dict['win'] += 1

        if res[0] == 4: # dealer busted
            # I have no fucking idea why Python just assumes that I want to split a string into
            # chars when I append it to a list here but WHATEVER.
            stats_dict['dealer_bust'] += [res[1]]
            stats_dict['win'] += 1

        # Add dealer's starting card frequencies
        stats_dict['dealer_card_freqs'] += [res[1]] 
    stats_dict['dealer_bust'] = sorted(stats_dict['dealer_bust'])
    stats_dict['dealer_card_freqs'] = sorted(stats_dict['dealer_card_freqs'])
    
    print(stats_dict)
    return stats_dict

""" Returns plt object and sanitized stats_dict """
def graph_data(trials: int, stats_dict: dict, fname: str) -> plt:
    y_ticks: int
    if trials > 10:
        y_ticks = range(0, trials, trials//10)
    else:
        y_ticks = range(0, 10)

    fig, ax = plt.subplots()
    # JFC what the hell am I doing
    bust_lst = stats_dict['dealer_bust']
    dealer_cards_when_dealer_bust = collections.Counter(bust_lst)
        
    bust_sum = sum(dealer_cards_when_dealer_bust.values())

    # Sanitize stats_dict output to contain the frequences
    stats_dict['dealer_bust'] = dealer_cards_when_dealer_bust
    rank_names = dealer_cards_when_dealer_bust.keys()
    rank_freqs = dealer_cards_when_dealer_bust.values()
    ax.bar(rank_names, rank_freqs)

    plt.title(f"Dealer Bust Freqs")
    ax.set_xticklabels((list(rank_names)))
    output_fname = f"{SAVE_DIR}/{fname}"
    plt.savefig(output_fname)
    
    stats_dict['dealer_card_freqs'] = collections.Counter(stats_dict['dealer_card_freqs'])
    freq_sum = sum(stats_dict['dealer_card_freqs'].values())
    stats_dict['dealer_card_freqs']['total'] = freq_sum

    # Add the total number of dealer busts to make calculating probabilities easier
    stats_dict['dealer_bust']['total'] = bust_sum
    print(f"Saved graph to {output_fname}")
    return plt, stats_dict

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

def check_data_dir():
    dirs = [d for d in os.listdir('.') if not os.path.isfile(d)]
    if SAVE_DIR not in dirs:
        os.makedirs(SAVE_DIR)
    for d in dirs:
        print(d)


DATA_FNAME = "bust-data"
if __name__ == "__main__":
    trials: int = 1000
    check_data_dir()
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
    
    # Please consult Josh if this is confusing and you have questions, I'm too lazy to do this properly
    graph_plt, stats_dict = graph_data(trials, stats_dict, plt_fname)

    dump_json(stats_dict, json_fname)
    # graph_plt.show()

    # h = Hand([Card('Clubs', 'Ace'), Card('Clubs', 'Ace'), Card('Clubs', 'Ace')])
    # h = Hand([Card('Clubs', 'Ace'), Card('Clubs', 'Ace')])
    # print(h.show_info())
    # print(total_value(h))
