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

    """ run with modified deck """
    # ranks = ["Ace", "9", "8"]
    # frequencies = [4, 3, 2]

    # remove all face cards
    ranks = ["jack", "queen", "king"]
    frequencies = [4, 4, 4]
    
    tester.next_path("foo", "bar")
    
    # stats_dict = tester.run_with_modified_deck(trials, ranks, frequencies)

    # tester.print_stats_dict(stats_dict)

    # np_thresh, np_loss, np_draw, np_win = tester.get_data_lists(stats_dict)
    
    # # Generate datetime string to use as output filename
    # dt_str = tester.get_datetime()

    # tester.graph_data(trials, np_thresh, np_loss, np_draw, np_win, ranks, frequencies, dt_str)
    
    # tester.dump_json(stats_dict, dt_str)

    
