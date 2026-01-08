def hand_value(hand):
    value = 0
    aces = 0
    for i in hand:
        rank, suit = i
        if rank in ['J', 'Q', 'K']:
            value += 10
        elif rank == 'A':
            aces += 1
            value += 11
        else:
            value += int(rank)
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def print_blackjack_rules():

    print(" BLACKJACK RULES \n")

    print("• Goal: Beat the dealer by getting a hand closer to 21 without busting (>21).")
    print("• Cards: 2-10 = face value, J/Q/K = 10, A = 1 or 11 (auto-best).")
    print("• 4-deck shoe (208 cards) shuffled randomly + Faro for realism.")
    print("• Start with $1000 bankroll. Bet 1-1000 each hand. Broke = game over.")
    print("• Wins pay 1:1 (double your bet). Ties (push) = bet returned. Losses/busts = lose bet.")
    print("• Dealer: Shows 1 card, hits <17, stands 17+.")
    print("• Insurance: When dealer shows A, bet half your main bet. Pays 2:1 if dealer has Blackjack.")
    print("• Your actions: Hit (h) = card, Stand (s) = done, Quit (q) = end game.")
    print("• No splitting/doubling (simple rules). Play smart!")
    print("• Have fun and gamble responsibly, good luck! :)\n")