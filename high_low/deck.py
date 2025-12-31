import random
cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
         'J': 11, 'Q': 12, 'K': 13, 'A': 14}
suits = ['♥', '♦', '♣', '♠']

def create_deck():
    return [(card, suit) for suit in suits for card in cards.keys()]

def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

def faro_shuffle(deck):
    half = len(deck) // 2
    first_half = deck[:half]
    second_half = deck[half:]
    return [card for pair in zip(first_half, second_half) for card in pair]

def draw_card(deck):
    return deck.pop(0)