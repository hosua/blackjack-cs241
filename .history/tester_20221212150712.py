from card_engine import *
from card_handler import *
from matplotlib import pyplot as plt
import numpy as np
import json
from datetime import datetime
import os

# Where all gathered data will be saved
SAVE_DIR = 'data'

"""
Note: If you are reading this, you should call the run() or run_with_modified_deck() functions, do not call
auto_play() directly. 

Runs hit_thresh number of trials. If a card_types value is passed, remove those card_types from the deck.
Hits when below hit threshhold.

Returns values:
0 - player lost
1 - draw
2 - player win

Only plays a single game, we should probably consider setting up different game scenarios as well
to make game decisions based on the cards remaining in the deck.
"""
### TODO: learn some numpy later so we can make some nice graphs ###
# array size = 20-2 = 18
def init_stats_dict():
    stats_dict = dict()
    for i in range(2,21):
        stats_dict[i] = {'lose': 0, 'draw': 0, 'win': 0}
    return stats_dict

def print_stats_dict(d: dict):
    for key in d:
        print(f"threshhold: {key}")
        for v in d[key]:
            print(f"{v} : {d[key][v]}", end="\t")
        print()

def auto_play(hit_thresh: int, card_types: dict=None) -> int:
    # Creates deck for game
    deck = Deck("Blackjack")

    player = Hand()
    dealer = Hand()

    # modify the deck if card_types parameter passed
    if card_types:
        deck.remove_from_deck(card_types)
    
    dealer_start(dealer, deck)
    player_start(player, deck)
    while True:
        if total_value(player) == 21:
            dealer_open(dealer)
            if total_value(dealer) != 21:
                print("Blackjack! Player wins!\n")
                return 2
            else:
                print("Tie!\n")
                return 1
        # below threshhold, hit
        if total_value(player) < hit_thresh:
            p_hit(player, deck)
            if total_value(player) == 21:
                dealer_open(dealer)
                if total_value(dealer) == 21:
                    print("Tie!\n")
                    return 1
                else:
                    print("Blackjack! Player wins!\n")
                    return 2
            elif total_value(player) > 21:
                print("Player bust! Player loses!\n")
                return 0
        # above threshhold, stand
        else:
            if total_value(dealer) < 17:
                while total_value(dealer) < 17:
                    d_hit(dealer, deck)

                if total_value(dealer) == total_value(player):
                    print("Tie!\n")
                    return 1
                elif total_value(dealer) == 21:
                    print("Player loses!\n")
                    return 0
                elif total_value(dealer) > 21:
                    print("Dealer bust! Player wins!\n")
                    return 2
                elif total_value(dealer) > total_value(player):
                    print("Player loses!\n")
                    return 0
                else:
                    print("Player wins!\n")
                    return 2
            else:
                dealer_open(dealer)
                if total_value(dealer) == total_value(player):
                    print("Tie!\n")
                    return 1
                if total_value(dealer) == 21:
                    print("Player loses!\n")
                    return 0
                if total_value(dealer) > 21:
                    print("Dealer bust! Player wins!\n")
                    return 2
                if total_value(dealer) > total_value(player):
                    print("Player loses!\n")
                    return 0
                else:
                    print("Player wins!\n")
                    return 2
 

def run(trials: int) -> dict:
    stats_dict: dict
    thresh_min: int
    thresh_max: int
    res: int # 0 -> lose, 1 -> draw, 2 -> win

    stats_dict = init_stats_dict()
    thresh_min, thresh_max = 2, 20
    for thresh in range(thresh_min, thresh_max+1):
        for trial in range(trials):
            res = auto_play(thresh)
            if res == 0:
                stats_dict[thresh]['lose'] += 1
            elif res == 1:
                stats_dict[thresh]['draw'] += 1
            elif res == 2:
                stats_dict[thresh]['win'] += 1
    
    print(f"{trials} trials were ran with no modifications to the deck")
    return stats_dict

def run_with_modified_deck(trials: int, ranks: list[str], frequencies: list[int]) -> dict:

    if len(ranks) != len(frequencies):
        print("ERROR: length of frequences must match length of ranks")
        exit()     

    card_types = dict(zip(ranks, frequencies))

    stats_dict: dict
    thresh_min: int
    thresh_max: int
    res: int # 0 -> lose, 1 -> draw, 2 -> win

    stats_dict = init_stats_dict()
    thresh_min, thresh_max = 2, 20
    for thresh in range(thresh_min, thresh_max+1):
        for trial in range(trials):
            res = auto_play(thresh, card_types)
            if res == 0:
                stats_dict[thresh]['lose'] += 1
            elif res == 1:
                stats_dict[thresh]['draw'] += 1
            elif res == 2:
                stats_dict[thresh]['win'] += 1
            else:
                print("ERROR: trial didn't result in anything!") 
                exit()
    print("--------------------------------------------")
    print(f"{trials} trials were ran with the following modifications to the deck:")
    for i in range(len(ranks)):
        rank = ranks[i]
        freq = frequencies[i]
        print(f"Removed {freq} x {rank} cards\n")
    print("--------------------------------------------")
    return stats_dict

def get_data_lists(stats_dict: dict):
    thresh_lst = []
    loss_lst = []
    draw_lst = []
    win_lst = []
    for key in stats_dict:
        thresh_lst.append(key)
        loss_lst.append(stats_dict[key]['lose'])
        draw_lst.append(stats_dict[key]['draw'])
        win_lst.append(stats_dict[key]['win'])

    np_thresh = np.array(thresh_lst)
    np_loss = np.array(loss_lst)
    np_draw = np.array(draw_lst)
    np_win = np.array(win_lst)

    return np_thresh, np_loss, np_draw, np_win 

def graph_data(trials: int, np_thresh, np_loss, np_draw, np_win, ranks: list[str] frequencies: list[int], dt_str: str):
    x_ticks = range(2, 21)
    y_ticks = range(0, trials, int(trials/10))
    # x = np.arange(2,20)
    # y = 2*x+5
    output = ""
    for i in range(len(ranks)):
        output += f"Removed: {frequencies[i]} x {ranks[i]}"
    plt.title(f"Trials: {trials}\t{output}")
    plt.xticks(x_ticks)
    plt.yticks(y_ticks)
    plt.xlabel("Threshhold")
    plt.ylabel("Losses/Draws/Wins")
    plt.plot(np_thresh, np_loss, label='Losses')
    plt.plot(np_thresh, np_draw, label='Draws')
    plt.plot(np_thresh, np_win, label='Win')
    plt.legend(loc="upper right")
    output_fname = f"{SAVE_DIR}/{dt_str}.png"
    plt.savefig(output_fname)
    print(f"Saved graph to {output_fname}")
    plt.show()

""" Used for generating unique file name """
def get_datetime() -> str:
    curr_dt = datetime.now()
    dt_str = curr_dt.strftime("%Y-%m-%d_%H-%M-%S")
    return dt_str

""" Dump stats_dict into json file """
def dump_json(stats_dict: dict, dt_str: str):

    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)

    output_fname = f"{SAVE_DIR}/{dt_str}.json"

    with open(output_fname, "w") as f:
        json.dump(stats_dict, f, indent=2)
    print(f"Dumped data to {output_fname}")
    


