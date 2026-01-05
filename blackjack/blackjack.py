from blackjack.hand_val import hand_value
from high_low.deck import *

def play_blackjack():
    print("\n Welcome to Blackjack! (4-Deck Game to counter card counters :) )\n")

    deck = create_deck() * 4
    shuffle_deck(deck)

    # Deal initial cards
    player_hand = [draw_card(deck), draw_card(deck)]
    dealer_hand = [draw_card(deck), draw_card(deck)]

    # === PLAYER TURN ===
    while hand_value(player_hand) < 21:
        print(f"Your hand:  {[f'{c[0]}{c[1]}' for c in player_hand]} → {hand_value(player_hand)}")
        print(f"Dealer shows: {dealer_hand[0][0]}{dealer_hand[0][1]} (and one hidden card)\n")

        action = input("Hit (h), Stand (s), or Quit (q)? ").strip().lower()

        if action not in ['h', 's', 'q']:
            print("Invalid! Please enter 'h', 's', or 'q'.")
            continue

        if action == 'q':
            print("Thanks for playing!")
            return

        if action == 'h':
            player_hand.append(draw_card(deck))
            if hand_value(player_hand) > 21:
                print(f"You drew: {player_hand[-1][0]}{player_hand[-1][1]}")
                print(f"Your hand: {[f'{c[0]}{c[1]}' for c in player_hand]} → {hand_value(player_hand)}")
                print(" BUST! You went over 21. Dealer wins.")
                return
        else:  #  this is for stand
            break

    # dealer's turn - just in case player hasn't busted
    player_score = hand_value(player_hand)
    if player_score <= 21:
        print("\nDealer reveals hidden card...")
        print(f"Dealer hand: {[f'{c[0]}{c[1]}' for c in dealer_hand]} → {hand_value(dealer_hand)}")


        while hand_value(dealer_hand) < 17:
            print("Dealer hits...")
            dealer_hand.append(draw_card(deck))
            print(f"Dealer draws: {dealer_hand[-1][0]}{dealer_hand[-1][1]}")
            print(f"Dealer total: {hand_value(dealer_hand)}")

        dealer_score = hand_value(dealer_hand)

        # final results - compare scores
        print("\n" + "="*30)
        print(f"Your score:   {player_score}")
        print(f"Dealer score: {dealer_score}")
        print("="*30)

        if dealer_score > 21:
            print(" HEHE Dealer BUSTED! You win!")
        elif dealer_score > player_score:
            print(" Dealer wins. *(sad trombone sound)*")
        elif dealer_score < player_score:
            print(" You win! :) Congratulations!")
        else:
            print(" Push (tie)! Money back.")

    # Optional: Play again?
    print("\n" + "-"*30)
    if input("Play another hand? (y/n): ").strip().lower() == 'y':
        play_blackjack()  # Recursive call — simple way to restart


# Run the game
if __name__ == "__main__":
    play_blackjack()