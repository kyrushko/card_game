# python
from blackjack.hand_val import hand_value, print_blackjack_rules
from high_low.deck import *

# Simple betting system
DEFAULT_BANKROLL = 1000


# python
def play_blackjack():
    print_blackjack_rules()
    print("\n Welcome to Blackjack! (4-Deck Game because we are a cool casino)\n")
    deck = create_deck() * 4
    shuffle_deck(deck)
    faro_shuffle(deck)
    print("Deck shuffled! Let's play.\n")
    bankroll = DEFAULT_BANKROLL
    print(f"Starting bankroll: ${bankroll}\n")

    last_bet = None

    while bankroll > 0:
        print(f"Current bankroll: ${bankroll}")

        while True:
            raw = input(f"Place your bet (1-${bankroll}): ").strip()
            # allow empty input to reuse last bet (if still valid)
            if raw == '' and last_bet is not None and 1 <= last_bet <= bankroll:
                bet = last_bet
                break
            if not raw.isdigit():
                print("Enter a number!")
                continue
            bet = int(raw)
            if 1 <= bet <= bankroll:
                last_bet = bet
                break
            print("Invalid bet amount!")

        # Deduct main bet immediately
        bankroll -= bet

        # Deal
        player_hand = [draw_card(deck), draw_card(deck)]
        dealer_hand = [draw_card(deck), draw_card(deck)]

        print(f"\nYour hand: {[f'{c[0]}{c[1]}' for c in player_hand]} → {hand_value(player_hand)}")
        print(f"Dealer shows: {dealer_hand[0][0]}{dealer_hand[0][1]}")

        insurance_bet = 0
        if dealer_hand[0][0] == 'A':
            print("\nDealer has Ace → Insurance offered!")
            ins_choice = input("Buy insurance? (y/n): ").strip().lower()
            if ins_choice == 'y' and bet * 0.5 <= bankroll:
                insurance_bet = bet // 2
                bankroll -= insurance_bet
                print(f"Insurance bet: ${insurance_bet}")

        # Player turn
        busted = False
        while hand_value(player_hand) < 21:
            action = input("\nHit (h), Stand (s), Quit (q)? ").strip().lower()
            if action == 'q':
                print("Quitting game. Goodbye!")
                return
            if action not in ['h', 's']:
                print("Invalid! 'h' or 's'")
                continue
            if action == 'h':
                player_hand.append(draw_card(deck))
                print(f"You drew: {player_hand[-1][0]}{player_hand[-1][1]}")
                print(f"Hand: {[f'{c[0]}{c[1]}' for c in player_hand]} → {hand_value(player_hand)}")
                if hand_value(player_hand) > 21:
                    print(" BUST!")
                    busted = True
                    break
            else:
                break

        # Resolve insurance first (if any)
        if insurance_bet > 0:
            if hand_value(dealer_hand) == 21:  # Dealer Blackjack
                print(f"Dealer has Blackjack! Insurance pays 2:1 → +${insurance_bet * 2}")
                bankroll += insurance_bet * 3  # Return stake + win (2:1)
            else:
                print("No dealer Blackjack → Insurance lost")
                # Insurance stake already deducted

        # If player busted → lose main bet (already deducted)
        if busted:
            print(f"You lose your ${bet} bet.")
            # If bankroll reached 0 after deducting the bet, announce & end game
            if bankroll == 0:
                print("\nYou're out of money! Game over.")
                break
            print("\n" + "-"*40)
            # Play again?
            if input("\nPlay another hand? (y/n): ").strip().lower() != 'y':
                print(f"\nThanks for playing! Final bankroll: ${bankroll}")
                break
            continue

        # Dealer turn
        print("\nDealer reveals hidden card...")
        print(f"Dealer hand: {[f'{c[0]}{c[1]}' for c in dealer_hand]} → {hand_value(dealer_hand)}")
        while hand_value(dealer_hand) < 17:
            dealer_hand.append(draw_card(deck))
            print(f"Dealer hits: {dealer_hand[-1][0]}{dealer_hand[-1][1]} → {hand_value(dealer_hand)}")

        player_score = hand_value(player_hand)
        dealer_score = hand_value(dealer_hand)

        # Payouts
        print("\n" + "="*40)
        if dealer_score > 21:
            print("Dealer BUSTED → You win!")
            bankroll += bet * 2  # Return stake + win
        elif player_score > dealer_score:
            print("You win!")
            bankroll += bet * 2
        elif player_score == dealer_score:
            print("Push → Bet returned")
            bankroll += bet  # Return stake
        else:
            print("Dealer wins → You lose your bet")
            # Bet already deducted

        print(f"New bankroll: ${bankroll}")
        print("="*40)

        if bankroll == 0:
            print("\nYou're out of money! Game over.")
            break

        # Play again?
        if input("\nPlay another hand? (y/n): ").strip().lower() != 'y':
            print(f"\nThanks for playing! Final bankroll: ${bankroll}")
            break


if __name__ == "__main__":
    play_blackjack()
