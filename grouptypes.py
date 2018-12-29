# Note: there are exception handling for UnboundLocalErrors, in the event
# where the group has all aces.


def phasedout_group_type(group):
    """ Determine the type of group of cards based on the conditions given
    below that satisfies the phases for the game "Phased Out". Consider the
    number of cards that satisfies the value, suit, colour of the first card
    along with a check of valid run formation.
    """

    # Provide a list of the card's values and suits.
    numberlist = []
    suitlist = []
    # The first card will be the anchor for groups 1, 2 and 3. num and suit
    # will increment if the subsequent cards have the same number or suit
    # of the first card, respectively.
    num = 1
    suit = 1
    # suitdict provides a dictionary for each suit's colour.
    suitdict = {"D": "R", "H": "R", "S": "B", "C": "B"}
    # Assume that the first card would satisfy either category by having count
    # equals to 1
    colour_count = 1
    straight_count = 1
    # naturals refer to non-Aces.
    naturals = 0
    # Define the numerical value for 0, J, Q and K useful for group 4 and 5
    for card in group:
        if card[0] == "0":
            numberlist.append("10")
        elif card[0] == "J":
            numberlist.append("11")
        elif card[0] == "Q":
            numberlist.append("12")
        elif card[0] == "K":
            numberlist.append("13")
        else:
            numberlist.append(card[0])
        suitlist.append(card[1])

    # Ace can be any numerical value, so acelist provides a repetition of a
    # possible value that can satisfy group 4 and 5
    acelist = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    # Check whether each card is a natural card.
    for natural_check in numberlist:
        if natural_check != "A":
            naturals += 1

    # Find the first number that is not an ace to be compared in check_num
    for natural_num in numberlist:
        if natural_num != "A":
            first_num = natural_num
            break

    # Find the first suit that is not an ace to be compared in check_suit
    for natural_suit in range(0, len(suitlist)):
        if numberlist[natural_suit] != "A":
            first_suit = suitlist[natural_suit]
            break

    # check_num is used to satisfy either groups 1 or 3
    for check_num in range(1, len(numberlist)):
        try:
            if (first_num == numberlist[check_num] or
                    numberlist[check_num] == "A"):
                    num += 1
        except UnboundLocalError:
            break

    # check_suit is used to satisfy group 2 for suit, and determine its colour
    # used to satisfy group 5
    for check_suit in range(1, len(suitlist)):
        try:
            if (suitdict[first_suit] == suitdict[suitlist[check_suit]] or
                    numberlist[check_suit] == "A"):
                colour_count += 1
            if (first_suit == suitlist[check_suit] or
                    numberlist[check_suit] == "A"):
                suit += 1
        except UnboundLocalError:
            break

    # If the first card is an ace, check the value of the ace that will satisfy
    # the run for group 4.
    current_ace = 1
    if numberlist[0] == "A":
        increase = 1
        for index in range(1, len(numberlist)):
            if numberlist[index] != "A":
                current_ace = int(numberlist[index]) - increase
                # in the case of ace values 1 or lower, nullify group 4/5
                if current_ace <= 1:
                    straight_count = 0
                break
            increase += 1

    # check_straight is used to satisfy group 4/5.
    for check_straight in range(1, len(numberlist)):
        if (numberlist[check_straight] == "A" and
                numberlist[check_straight-1] != "A"):
            for ace in acelist:
                # check if the current ace satisfies the run of cards.
                if int(numberlist[check_straight-1]) + 1 == int(ace):
                    current_ace = ace
                    straight_count += 1
                    # in the case of ace values 14 or higher, negate group 4/5
                    if current_ace >= 14:
                        straight_count = 0
                    break
        # if the current and previous cards are aces, safely assume that the
        # run still satisfies.
        elif (numberlist[check_straight] == "A" and
              numberlist[check_straight-1] == "A"):
            try:
                current_ace += 1
                straight_count += 1
                if current_ace >= 14:
                    straight_count = 0
                    break
            except UnboundLocalError:
                break
        # Check whether the current card is the increment of the current ace
        # (the previous card) if the current card is a non-Ace.
        elif numberlist[check_straight-1] == "A":
            if current_ace == int(numberlist[check_straight]) - 1:
                straight_count += 1
            else:
                break
        # Check whether the run continues in the case of non-Aces
        else:
            if (int(numberlist[check_straight-1]) + 1 ==
                    int(numberlist[check_straight])):
                straight_count += 1

    # Determine group types based on the conditions met
    if num == 3 and naturals >= 2 and len(numberlist) == 3:
        return 1
    elif suit == 7 and naturals >= 2 and len(numberlist) == 7:
        return 2
    elif num == 4 and naturals >= 2 and len(numberlist) == 4:
        return 3
    elif straight_count == 8 and naturals >= 2 and len(numberlist) == 8:
        return 4
    elif (colour_count == 4 and naturals >= 2 and straight_count == 4 and
          len(numberlist) == 4):
        return 5
    else:
        return None
