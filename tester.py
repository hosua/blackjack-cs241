from card_engine import *
from handler import *
import numpy as np
"""
Trial tester
Hits when below hit threshhold
Returns values:
0 - player lost
1 - draw
2 - player win

***
Only plays a single game, we should probably consider setting up different game scenarios as well
to make game decisions based on the cards remaining in the deck.
***

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

def auto_play(hit_thresh: int) -> int:
    # Creates deck for game
    deck = Deck("Blackjack")

    player = Hand()
    dealer = Hand()

    dealer_start(dealer, deck)
    player_start(player, deck)
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

    return stats_dict

