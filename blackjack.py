'''
A simple blackjack game
'''

import time
import collections
from card_style import make_card
from card_engine import *
import tester


if __name__ == "__main__":
    # number of trials
    trials = 1000


    """ run without modified deck """
    # stats_dict = tester.run(trials)

    """ run with modified deck """
    ranks = ["Ace", "9", "8"]
    frequencies = [4, 3, 2]
    
    stats_dict = tester.run_with_modified_deck(trials, ranks, frequencies)

    tester.print_stats_dict(stats_dict)
    
