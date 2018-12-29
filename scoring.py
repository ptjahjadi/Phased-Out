def phasedout_score(hand):
    """ Determine the total score for the hand (assuming the game has ended)
    based on the rules of "Phased Out".
    """
    score = 0
    # Determine the value of each card in the hand, and add to score
    for card in hand:
        if card[0] == "0":
            score += 10
        elif card[0] == "J":
            score += 11
        elif card[0] == "Q":
            score += 12
        elif card[0] == "K":
            score += 13
        elif card[0] == "A":
            score += 25
        else:
            score += int(card[0])
    return score
