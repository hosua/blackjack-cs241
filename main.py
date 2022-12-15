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
import sys

""" You can enter the number of trials as a command line argument (default 1) """

if __name__ == "__main__":
    trials: int = 1000

    if len(sys.argv) > 1:
        try:
            trials = int(sys.argv[1])
        except ValueError:
            print("Error: Argument must be an integer")
            exit(1)

    DATA_FNAME = f"T{trials}"
    
    # get next available file name
    json_fname = tester.get_next_name(DATA_FNAME, "json")
    plt_fname = tester.get_next_name(DATA_FNAME, "png")

    """ run without modified deck """
    # stats_dict = tester.run(trials)
    # np_thresh, np_loss, np_draw, np_win = tester.get_data_lists(stats_dict)
    # graph_plt = tester.graph_data(trials, np_thresh, np_loss, np_draw, np_win, plt_fname)

    """ run with modified deck """
    # remove all face cards
    ranks = ["jack", "queen", "king"]
    frequencies = [4, 4, 4]
    stats_dict = tester.run_with_modified_deck(trials, ranks, frequencies)

    tester.print_stats_dict(stats_dict)
    
    np_thresh, np_loss, np_draw, np_win = tester.get_data_lists(stats_dict)
    graph_plt = tester.graph_data(trials, np_thresh, np_loss, np_draw, np_win, plt_fname, ranks, frequencies)
    
    # plt.show() # comment this out if you want to run tests without stopping
    tester.dump_json(stats_dict, json_fname)

    
