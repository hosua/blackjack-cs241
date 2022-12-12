'''
A simple blackjack game
'''

import time
import collections
from card_style import make_card
from card_engine import *
import tester

# Play
def play():
    print("Welcome to BlackJack!")
    print("---------------------")
    while True:
        # Creates deck for game
        deck = Deck("Blackjack")

        # Creates player and dealer hands
        player = Hand()
        dealer = Hand()

        dealer_start(dealer, deck)
        player_start(player, deck)
    
        while True:
            if total_value(player) == 21:
                dealer_open(dealer)
                if total_value(dealer) != 21:
                    print("Blackjack! Player wins!\n")
                    break
                else:
                    print("Tie!\n")
                    break
            choice = input("\nH to hit, S to stand, Q to quit\n")
            if choice.lower() == 'h':
                p_hit(player, deck)
                if total_value(player) == 21:
                    dealer_open(dealer)
                    if total_value(dealer) == 21:
                        print("Tie!\n")
                        break
                    else:
                        print("Blackjack! Player wins!\n")
                        break
                elif total_value(player) > 21:
                    print("Player bust! Dealer wins!\n")
                    break

            if choice.lower() == 's':
                if total_value(dealer) < 17:
                    while total_value(dealer) < 17:
                        d_hit(dealer, deck)
                        time.sleep(1.5)
                    if total_value(dealer) == total_value(player):
                        print("Tie!\n")
                        break 
                    if total_value(dealer) == 21:
                        print("Dealer wins!\n")
                        break    
                    if total_value(dealer) > 21:
                        print("Dealer bust! Player wins!\n")
                        break    
                    if total_value(dealer) > total_value(player):
                        print("Dealer wins!\n")
                        break    
                    else:
                        print("Player wins!\n")
                        break
                else:
                    dealer_open(dealer)
                    if total_value(dealer) == total_value(player):
                        print("Tie!\n")
                        break
                    if total_value(dealer) == 21:
                        print("Dealer wins!\n")
                        break
                    if total_value(dealer) > 21:
                        print("Dealer bust! Player wins!\n")
                        break
                    if total_value(dealer) > total_value(player):
                        print("Dealer wins!\n")
                        break
                    else:
                        print("Player wins!\n")
                        break

            if choice.lower() == 'q':
                print("Thanks for playing, goodbye!\n")
                quit()
            continue
        print("----------- Next Round -----------")
        time.sleep(2)
        continue


if __name__ == "__main__":
    
    # Run n trials
    n = 1000
    stats_dict = tester.run(n)
    tester.print_stats_dict(stats_dict)
    
