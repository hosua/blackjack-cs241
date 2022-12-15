import time
import collections
from card_style import *
from card_engine import *

def value(hand):
    value = 0
    cards = hand.get_hand()
    if len(cards[0].get_rank()) > 2 and cards[0].get_rank() != 'Ace':
        value += 10
    elif cards[0].get_rank() == 'Ace':
        value += 11
    else:
        value += int(cards[0].get_rank())
    return value

def ranks(hand):
    ranks = []
    for card in hand.get_hand():
        ranks.append(card.get_rank())
    return ranks

### Check if hand contains aces. This is used to check if the hand is a hard hand or a limp hand ###
def has_aces(hand) -> bool:
    for card in hand.get_hand():
        if card.get_rank() == 'Ace':
            # print("HAS ACES")
            return True
    # print("NO ACES")
    return False

def duplicate(ranks):
    if len(ranks) != len(set(ranks)):
        return True
    else:
        return False

# Returns true if there are multiple aces
def m_aces(counter):
    dupes = []
    for key in counter.keys():
        # if the count of the rank is greater than one
        if counter[key] > 1:
            # add it as a duplicate
            dupes.append(key)
    # If there are duplicate aces, return true
    if 'Ace' in dupes:
        return True
    else:
        return False

# This function calculates the minimum value of a hand
def calc_value(hand):
    value = 0
    for card in hand.get_hand():
        # this sums up all cards that are not aces or number cards
        if len(card.get_rank()) > 2 and card.get_rank() != 'Ace':
            value += 10
        # but if it is an ace, add one point only (because we already went over 21, and want to minimize our score
        elif card.get_rank() == 'Ace':
            value += 1
        # non-face/ace, add its value
        else:
            value += int(card.get_rank())
    return value

def check_hard(hand: Hand) -> bool:
    min_val = calc_value(hand)
    print(f"min_val: {min_val}")
    # print(f"has aces: {has_aces(hand)}")
    if not has_aces(hand):
        return True 
    # If the player has a hand such that their hand can still consider valuing an
    # ace at 11 without losing, the player has a soft hand
    return False if min_val + 11 <= 21 else True 

# returns total_score
def total_value(hand) -> int:
    value = 0
    for card in hand.get_hand():
        # if len(card.get_rank()) > 2, that means that it must a face card/ace
        if len(card.get_rank()) > 2 and card.get_rank() != 'Ace':
            value += 10
        elif card.get_rank() == 'Ace':
            value += 11
        else:
            value += int(card.get_rank())

        if value > 21:
            if duplicate(ranks(hand)):
                # returns dict of key (item being counted) and val (the count)
                counter = collections.Counter(ranks(hand))

                # if there are multiple aces
                if m_aces(counter):
                    value = calc_value(hand)
                    value += 10
                    if value > 21:
                        return calc_value(hand)
                else:
                    return calc_value(hand)
            # No duplicates, which must entail that we still have a soft hand
            else:
                return calc_value(hand)
    return value
            
def player_start(hand, deck):
    '''
    drew = []
    a = Card('Clubs', '5')
    b = Card('Diamonds', '3')
    drew.append(a)
    drew.append(b)
    '''
    drew = deck.draw_cards(2)
    hand.add_cards(drew)
    if not HIDE_OUTPUT:
        print('Player hand:', total_value(hand))
        hand.show_info()

def dealer_start(hand, deck):
    drew = deck.draw_cards(2)
    hand.add_cards(drew)
    if not HIDE_OUTPUT:
        print('\nDealer hand:', value(hand))
        hand.show_info(1)

def dealer_open(hand):
    if not HIDE_OUTPUT:
        print('\nDealer hand:', total_value(hand))
        hand.show_info()

def p_hit(hand, deck):
    '''
    draw = []
    a = Card('Hearts', '5')
    b = Card('Spades', '3')
    c = Card('Diamonds', 'Ace')
    draw.append(a)
    draw.append(b)
    draw.append(c)
    '''
    draw = deck.draw_card()
    hand.add_card(draw)
    
    if not HIDE_OUTPUT:
        print('\nPlayer hand:', total_value(hand))
        hand.show_info()

def d_hit(hand, deck):
    draw = deck.draw_card()
    hand.add_card(draw)
    if not HIDE_OUTPUT:
        print('\nDealer hand:', total_value(hand))
        hand.show_info()
