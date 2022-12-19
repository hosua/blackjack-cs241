from matplotlib import pyplot as plt
import numpy as np
import json
import sys

# Make pie chart for dealer bust frequencies
def json_to_pie(fname: str):
    data: dict
    with open(fname) as json_data:
        data = json.load(json_data)
    
    dealer_bust_freq_data = data['dealer_bust']
    dealer_card_totals = data['dealer_card_freqs']
    
    dealer_bust_freq_data.pop('total')

    rank_names = dealer_bust_freq_data.keys()
    rank_freqs = dealer_bust_freq_data.values()
    rank_totals = dealer_card_totals.values()

    fig = plt.figure(figsize=(10,7))
    # print(rank_freqs, rank_names)
    plt.title("Dealer Bust Rates Per Card")
    # plt.pie(rank_freqs, autopct='%1.2f%%', textprops={'fontsize': 8})
    rank_percents = [(p/t)*100 for p, t in zip(rank_freqs, rank_totals) ]
    
    plt.pie(rank_freqs, textprops={'fontsize': 8})
    rank_names = ['%s, %1.1f%%' % (l, s) for l, s in zip(rank_names,rank_percents)]
    # rank_names = ['{, {s:0.1f}%' for l, s in zip(rank_names, rank_freqs)]
    plt.legend(labels=rank_names, loc="right", bbox_to_anchor=(1.3,0.8))

    plt.savefig("dealer-bust-rates-pie-chart.png")
    plt.show()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Please enter the json file as argument")
        exit()
    
    fname = sys.argv[1]
    json_to_pie(fname)
