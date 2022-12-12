'''
A simple blackjack game
'''

import time
import collections
from card_style import make_card
from card_engine import *
from matplotlib import pyplot as plt
import tester
import numpy as np


if __name__ == "__main__":
    # number of trials
    trials = 1000


    """ run without modified deck """
    # stats_dict = tester.run(trials)

    """ run with modified deck, note that all face cards are already removed """
    # ranks = ["Ace", "9", "8"]
    # frequencies = [4, 3, 2]
    ranks = []
    frequencies = []
    
    stats_dict = tester.run_with_modified_deck(trials, ranks, frequencies)

    tester.print_stats_dict(stats_dict)

    np_thresh, np_loss, np_draw, np_win = tester.get_data_lists(stats_dict)
    
    tester.graph_data(trials, np_thresh, np_loss, np_draw, np_win)

    print(thresh_lst)
    
