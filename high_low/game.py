from .deck import *

def is_higher(card1, card2):
    return cards[card2[0]] > cards[card1[0]]

def is_lower(card1, card2):
    return cards[card2[0]] < cards[card1[0]]

def play_game():
    print("\n HIGHER OR LOWER RULES ")
    print("• Goal: Guess if the next card is Higher or Lower than the current one.")
    print("• You play through the ENTIRE deck (all 51 remaining cards after the first) - or you can quit any time.")
    print("• Correct guess: Streak increases.")
    print("• Wrong guess: Game continues, streak stays the same - I wanted it soft hehe.")
    print("• Ties (same rank) count as wrong.")
    print("• Type 'q' at any time to quit early.")
    print("• At the end: See your longest streak, total correct guesses, and if you got a perfect run!")
    print("• Card ranks: 2 lowest → Ace highest (A=14). Suits don't matter.")
    print("• Multi-deck option available for marathon games!\n")

    while True:
        try:
            decks = input("How many decks? (1-8): ").strip()
            if decks.lower() == 'q':
                return
            num_decks = int(decks)
            if 1 <= num_decks <= 8:
                break
            print("Choose 1-8!")
        except:
            print("Enter a number!")

    deck = create_deck() * num_decks


    get_shuffle = input("How do you want to shuffle?\nF - Faro shuffle\nR - Random shuffle\n> ").strip().lower()
    if get_shuffle == 'f' and 'faro_shuffle' in globals():
        for _ in range(12):
            faro_shuffle(deck)
        print("Deck shuffled using Faro shuffle!\n")
    else:
        shuffle_deck(deck)
        print("Deck shuffled randomly!\n")

    current_card = draw_card(deck)
    streak = 0
    best_streak = 0
    total_correct = 0
    total_guesses = len(deck)

    print(f"Starting card: {current_card[0]}{current_card[1]} (value: {cards[current_card[0]]})\n")

    while deck:
        print(f"Cards left: {len(deck)} | Current streak: {streak} | Best: {best_streak}")
        print(f"Current: {current_card[0]}{current_card[1]} (value: {cards[current_card[0]]})")

        while True:
            guess = input("\nHigher (h), Lower (l), or Quit (q)? ").strip().lower()
            if guess in ('h', 'l', 'q'):
                break
            print("Invalid! Type 'h', 'l', or 'q'.")

        if guess == 'q':
            print(f"\nGame quit early!")
            break

        next_card = draw_card(deck)
        print(f"Next: {next_card[0]}{next_card[1]} (value: {cards[next_card[0]]})")

        correct = (guess == 'h' and is_higher(current_card, next_card)) or \
                  (guess == 'l' and is_lower(current_card, next_card))

        if correct:
            streak += 1
            total_correct += 1
            best_streak = max(best_streak, streak)
            print(f" Correct! Streak: {streak}\n")
        else:
            print(f" Wrong! Streak stays at {streak}\n")


        current_card = next_card


    print(" GAME OVER! FINAL STATS ")

    print(f"Total guesses: {total_guesses}")
    print(f"Correct answers: {total_correct}/{total_guesses}")
    print(f"Best streak: {best_streak}")
    print(f"Final streak: {streak}")

    if total_correct == total_guesses:
        print(" PERFECT RUN! You never missed! LEGENDARY! ")
    elif best_streak >= 20:
        print(" Amazing streak! You're on fire! ")

    print("\nThanks for playing!\n")