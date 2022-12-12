import time
import collections
from card_style import *
from card_engine import *
import tester

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

def duplicate(ranks):
    if len(ranks) != len(set(ranks)):
        return True
    else:
        return False

def m_aces(counter):
    dupes = []
    for key in counter.keys():
        if counter[key] > 1:
            dupes.append(key)
    if 'Ace' in dupes:
        return True
    else:
        return False

def calc_value(hand):
    value = 0
    for card in hand.get_hand():
        if len(card.get_rank()) > 2 and card.get_rank() != 'Ace':
            value += 10
        elif card.get_rank() == 'Ace':
            value += 1
        else:
            value += int(card.get_rank())
    return value
 
def total_value(hand):
    value = 0
    for card in hand.get_hand():
        if len(card.get_rank()) > 2 and card.get_rank() != 'Ace':
            value += 10
        elif card.get_rank() == 'Ace':
            value += 11
        else:
            value += int(card.get_rank())

        if value > 21:
            if duplicate(ranks(hand)):
                counter = collections.Counter(ranks(hand))
                if m_aces(counter):
                    value = calc_value(hand)
                    value += 10
                    if value > 21:
                        return calc_value(hand)
                else:
                    return calc_value(hand)
            else:
                return calc_value(hand)
    return value
            
def player_start(hand, deck):
    global HIDE_OUTPUT
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
    print('\nDealer hand:', value(hand))
    hand.show_info(1)

def dealer_open(hand):
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
    print('\nPlayer hand:', total_value(hand))
    hand.show_info()

def d_hit(hand, deck):
    draw = deck.draw_card()
    hand.add_card(draw)
    print('\nDealer hand:', total_value(hand))
    hand.show_info()
