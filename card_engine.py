'''
Card engine that generates a deck of cards
'''
from card_style import make_card
import random

# Dicts for suits and ranks of cards
SUITS = {0: "Clubs",
         1: "Diamonds",
         2: "Hearts",
         3: "Spades"
        }

RANKS = {1: "Ace",
         2: "2",
         3: "3",
         4: "4",
         5: "5",
         6: "6",
         7: "7",
         8: "8",
         9: "9",
         10: "10",
         11: "Jack",
         12: "Queen",
         13: "King"
        }

RANK_NUM = {
    "Ace": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5, 
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 11,
    "Queen": 12,
    "King": 13
}

# Creates a card object
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

# Creates a deck object, init a fresh new deck when created
class Deck:
    def __init__(self, name, removed=False):
        self.name = name
        self.deck = []
        self.create_deck(removed)
    
    # Creates the deck by adding cards into self.deck
    def create_deck(self, removed=False):
        # Refreshes the deck
        self.deck = []

        # Add cards to the deck
        for i in range(len(SUITS)):
            if removed:
                for j in range(1, 11):
                    self.deck.append(Card(SUITS[i], RANKS[j]))
            else:
                for j in range(1, 14):
                    self.deck.append(Card(SUITS[i], RANKS[j]))

        self.shuffle()
    
    # Shuffle the deck
    def shuffle(self):
        random.shuffle(self.deck)
        return self.deck
    
    # Show all cards in current deck, passes choice argument for face up or down cards
    def show_info(self, choice='u'):
        if len(self.deck) == 0:
            print("\nNo cards left in deck, resetting deck")
            self.create_deck()

        elif choice == 'u':
            print_neutral(self.deck)
        elif choice == 'd':
            print_face_down(self.deck)
    
    # Returns the no. of cards in the deck
    def get_len_deck(self):
        return len(self.deck)
    
    # Pop a card from deck and returns a card
    def draw_card(self):
        if len(self.deck) == 0:
            print("\nNo cards left in deck, resetting deck.")
            self.create_deck()
        else:
            drawn_card = self.deck.pop()
            # print("\nYou drew a card. (Show hand to show card drawn)")

            return drawn_card
    
    # Pop a specified no. of cards and return a list of cards
    def draw_cards(self, num_cards):
        drawn_cards = []
        if len(self.deck) < num_cards:
            print("\nNot enough cards left in deck, resetting deck.")
            self.create_deck()
        else:
            for i in range(num_cards):
                drawn_cards.append(self.deck.pop())
            # print("\nCards drawn. (Show hand to show cards drawn)")

        return drawn_cards

# Create cards on hand, optional: takes a list of cards as argument
class Hand:
    def __init__(self, hand=None):
        if hand is None:
            self.hand = []
        else:
            self.hand = hand
    
    def get_hand(self):
        return self.hand

    # Append a card to the list of cards in hand
    def add_card(self, card):
        self.hand.append(card)

    # Append a list of cards to the list of cards in hand
    def add_cards(self, cards):
        self.hand.extend(cards)
    
    # Show all the cards in hand
    def show_info(self, num=0):
        if len(self.hand) == 0:
            print("\nNo cards in hand")
        elif len(self.hand) == 1:
            if num > 0:
                self.hand[0] = Card("C", "Covered")
                print("\nCards in hand:")
                print("\n".join(map("".join, zip((make_card(self.hand[0]))))))
        else:
            if num > 0:
                print_neutral(card_specified(self.hand, num)) 
            else:
                print_neutral(self.hand)

    # Returns the no. of cards on hand
    def get_len_hand(self):
        return len(self.hand)

    # Clears cards in hand
    def reset_hand(self):
        self.hand = []


# Returns a list of card with specified number of face up and face down cards
def card_specified(cards, num):
    opened_list = []
    closed_list = []
    
    # Add face up cards to opened_list
    for x in range(len(cards) - num):
        opened_list.append(cards[x])

    # Add face down cards to closed_list
    for y in range(num):
        closed_list.append(Card("C", "Covered"))

    # Add face down cards into list with face up cards
    opened_list.extend(closed_list)

    return opened_list


# Prints out all cards faced up, formatted 9 per row. Takes a list of cards as argument
def print_neutral(cards):
    limit = 9    # slice end point
    start = 0    # slice start point
    length = len(cards)

    while True:
        if length < 10 and length != 0:
            print("\n".join(map("".join, zip(*(make_card(c) for c in cards[start:limit])))))
            break
        elif length == 0:
            break
        else:
            print("\n".join(map("".join, zip(*(make_card(c) for c in cards[start:limit])))))
            length -= 9
            start += 9    
            limit += 9
            

# Prints out all cards faced down, formatted 9 per row. Takes a list of cards as argument
def print_face_down(cards):
    limit = 9   # slice end point
    start = 0   # slice start point
    covered = []
    length = len(cards)

    # Makes a new list of all face down cards
    for i in range(length):
        covered.append(Card("C", "Covered"))

    while True:
        if length < 10 and length != 0:
            print("\n".join(map("".join, zip(*(make_card(c) for c in covered[start:limit])))))
            break
        elif length == 0:
            break
        else:
            print("\n".join(map("".join, zip(*(make_card(c) for c in covered[start:limit])))))
            length -= 9
            start += 9
            limit += 9

# Resets the deck and hand
def wipe(deck, hand):
    deck.create_deck()
    hand.reset_hand()
    print("\nHand and deck resetted")

# Call to run card engine tester in main
def play():

    deck = Deck("deck")
    hand = Hand()
    print("\nWelcome to the Card Engine!")
    print("---------------------------")

    while True:
        choice = input("\n1. Show deck\n2. Show hand\n3. Draw card(s)\n4. Shuffle deck\n"
                        + "5. Reset hand & deck\nQ. Quit\n\n")
        if choice == '1':
            while True:
                user = input("\nShow faced up or down? (U for up, D for down)\n")
                if (user.lower() != 'u') and (user.lower() != 'd'):
                    continue
                else:
                    deck.show_info(user.lower())
                    break
        elif choice == '2':
            while True:
                if hand.get_len_hand() != 0:
                    user = input("\nHow many cards faced down?\n")
                    if not(user.isnumeric()):
                        continue
                    elif int(user) > hand.get_len_hand():
                        print("\nNot enough cards, pick a different number.\n")
                        continue
                    else:
                        hand.show_info(int(user))
                        break
                else:
                    hand.show_info()
                    break
        elif choice == '3':
            while True:
                user = input("\nDraw how many cards?\n")
                if not(user.isnumeric()):
                    continue
                elif int(user) == 1:
                    drew = deck.draw_card()
                    hand.add_card(drew)
                    break
                elif int(user) > 1:
                    drew = deck.draw_cards(int(user))
                    hand.add_cards(drew)
                    break
                else:
                    continue
        elif choice == '4':
            deck.shuffle()
            print("\nDeck shuffled.")
        elif choice == '5':
            wipe(deck, hand)
        elif choice.lower() == 'q':
            print("\nOkay bye.")
            quit()
        else:
            continue
 
