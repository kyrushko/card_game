from traceback import print_tb

from .deck import *
def is_higher(card1, card2):
    return cards[card2[0]] > cards[card1[0]]

def is_lower(card1, card2):
    return cards[card2[0]] < cards[card1[0]]

def play_game():
    deck = create_deck()
    shuffle_deck(deck)
    print(deck)
    get_shuffle=  input("How do you want to shuffle the deck? \n F- faro shuffle; R - random shuffle ").strip().lower()

    if get_shuffle == 'r':
        shuffle_deck(deck)
        print("Deck shuffled! Ready to play.\n")
    elif get_shuffle == 'f':
        faro_shuffle(deck)
        print("Deck shuffled using Faro shuffle! Ready to play.\n")
    else:
        print("Invalid shuffle option! Proceeding with random shuffle.\n")
        shuffle_deck(deck)


    current_card = draw_card(deck)
    streak = 0
    while deck:
        print(f"\nCards left: {len(deck)}   |   Current streak: {streak}")
        print(f"Current: {current_card[0]}{current_card[1]} "
              f"(value: {cards[current_card[0]]})")

        while True:
            guess = input("Higher (h), Lower (l), or Quit (q)? ").strip().lower()

            if guess in ('h', 'l', 'q'):
                break
            else:
                print("Invalid input! Please type only 'h', 'l', or 'q'.")

        if guess == 'q':
            print(f"\nGame quit. Final streak: {streak}")
            break


        next_card = draw_card(deck)
        print(f"Next: {next_card[0]}{next_card[1]} "
              f"(value: {cards[next_card[0]]})")


        if (guess == 'h' and is_higher(current_card, next_card)) or \
                (guess == 'l' and is_lower(current_card, next_card)):
            streak += 1
            print(f"Correct! Current streak: {streak}\n")
            current_card = next_card
        else:
            print(f"Wrong! Streak stays the same.")
            current_card = next_card
            print()
