# main.py
from high_low.game import play_game
from blackjack.blackjack import play_blackjack

def main_menu():
    print("\n🃏 CARD GAME COLLECTION 🃏\n")
    print("1. Higher or Lower (Full Deck Challenge)")
    print("2. Blackjack (4 Decks)")
    print("3. Quit")

    while True:
        choice = input("\nChoose a game (1-3): ").strip()

        if choice == '1':
            print("\n" + "="*40)
            play_game()  # You can add num_decks here if you want
        elif choice == '2':
            print("\n" + "="*40)
            play_blackjack()
        elif choice == '3' or choice.lower() == 'q':
            print("\nThanks for playing! Goodbye! 👋")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()