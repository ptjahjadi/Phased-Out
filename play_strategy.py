from itertools import combinations
from collections import defaultdict

# There are 5 functions to check validity of each group, similar to Q1.


def check_group1(group):
    """ This function checks the validity of group 1 in the combination
    of cards. This function acts similar to Q1 with less considerations and
    only focusing in group 1 validity.
    """
    numberlist = []
    num = 1
    naturals = 0
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
    for natural_check in numberlist:
        if natural_check != "A":
            naturals += 1
    for natural_num in numberlist:
        if natural_num != "A":
            first_num = natural_num
            break
    for check_num in range(1, len(numberlist)):
        try:
            if (first_num == numberlist[check_num] or
                    numberlist[check_num] == "A"):
                    num += 1
        except UnboundLocalError:
            break
    if num == 3 and naturals >= 2 and len(numberlist) == 3:
        return True
    else:
        return False


def check_group2(group):
    """ This function checks the validity of group 2 in the combination
    of cards. This function acts similar to Q1 with less considerations and
    only focusing in group 2 validity.
    """
    numberlist = []
    suitlist = []
    suit = 1
    naturals = 0
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
    for natural_check in numberlist:
        if natural_check != "A":
            naturals += 1
    for natural_suit in range(0, len(suitlist)):
        if numberlist[natural_suit] != "A":
            first_suit = suitlist[natural_suit]
            break
    for check_suit in range(1, len(suitlist)):
        try:
            if (first_suit == suitlist[check_suit] or
                    numberlist[check_suit] == "A"):
                suit += 1
        except UnboundLocalError:
            break
    if suit == 7 and naturals >= 2 and len(numberlist) == 7:
        return True
    else:
        return False


def check_group3(group):
    """ This function checks the validity of group 3 in the combination
    of cards. This function acts similar to Q1 with less considerations and
    only focusing in group 3 validity.
    """
    numberlist = []
    num = 1
    naturals = 0
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
    for natural_check in numberlist:
        if natural_check != "A":
            naturals += 1
    for natural_num in numberlist:
        if natural_num != "A":
            first_num = natural_num
            break
    for check_num in range(1, len(numberlist)):
        try:
            if (first_num == numberlist[check_num] or
                    numberlist[check_num] == "A"):
                    num += 1
        except UnboundLocalError:
            break
    if num == 4 and naturals >= 2 and len(numberlist) == 4:
        return True
    else:
        return False


def check_group4(group):
    """ This function checks the validity of group 4 in the combination
    of cards. This function acts similar to Q1 with less considerations and
    only focusing in group 4 validity. Moreover, the placement of Aces are
    considered here and the correct hand formation from the sorted combinations
    are formed.
    """
    naturals = []
    aces = []
    outputgroup = []
    valuedict = {"2": "2", "3": "3", "4": "4", "5": "5",
                 "6": "6", "7": "7", "8": "8", "9": "9",
                 "0": "10", "J": "11", "Q": "12",
                 "K": "13", "A": "25"}
    for card in group:
        if card[0] == "A":
            aces.append(card)
        else:
            naturals.append(card)
    valid = True
    if len(aces) > 6:
        return None
    outputgroup.append(naturals[0])
    # current_card refers to the value of the card currently, useful in a loop
    # later on.
    current_card = int(valuedict[naturals[0][0]])
    index = 1
    # The loop will put Ace wherever necessary in attempt to
    # satisfy the run.
    while index < 8:
        # while index < 8 assumes that all the cards are natural cards. In the
        # case of the naturals list being exhausted, perform exception handling
        # to consider only aces.
        try:
            if current_card + 1 == int(valuedict[naturals[index][0]]):
                outputgroup.append(naturals[index])
                current_card += 1
                index += 1
            elif aces != []:
                outputgroup.append(aces[0])
                current_card += 1
                aces.remove(aces[0])
            else:
                break
        except IndexError:
            if aces != []:
                outputgroup.append(aces[0])
                current_card += 1
                aces.remove(aces[0])
            else:
                break
    # Determine if the first Ace put values less than 2
    if outputgroup[0][0] == "A":
        increase = 1
        for index in range(1, len(outputgroup)):
            if outputgroup[index][0] != "A":
                current_ace = (int(valuedict[outputgroup[index][0]]) -
                               increase)
                if current_ace <= 1:
                    valid = False
                break
            increase += 1
    # Determine if the last Ace put values more than 13 (K)
    if outputgroup[-1][0] == "A":
        increase = 0
        for index in reversed(range(len(outputgroup))):
            if outputgroup[index][0] != "A":
                current_ace = (int(valuedict[outputgroup[index][0]]) +
                               increase)
                if current_ace >= 14:
                    valid = False
                break
            increase += 1
    # The function will return the valid run positions of the Aces.
    if valid is True and len(outputgroup) == 8:
        return outputgroup
    else:
        return None

# This function checks the validity of group 5 in the combination of cards.


def check_group5(group):
    """ This function checks the validity of group 5 in the combination
    of cards. This function acts similar to Q1 with less considerations and
    only focusing in group 5 validity. Moreover, the placement of Aces are
    considered here and the correct hand formation from the sorted combinations
    are formed.
    """
    # Same functionality as check_group4 with the addition of colour check.
    suitdict = {"S": "B", "C": "B", "D": "R", "H": "R"}
    naturals = []
    aces = []
    outputgroup = []
    valuedict = {"2": "2", "3": "3", "4": "4", "5": "5",
                 "6": "6", "7": "7", "8": "8", "9": "9",
                 "0": "10", "J": "11", "Q": "12",
                 "K": "13", "A": "25"}
    for card in group:
        if card[0] == "A":
            aces.append(card)
        else:
            naturals.append(card)
    valid = True
    if len(aces) > 2:
        return None
    outputgroup.append(naturals[0])
    current_card = int(valuedict[naturals[0][0]])
    colour = suitdict[naturals[0][1]]
    # Check whether all natural cards satisfy the coloured run.
    for card in naturals:
        if suitdict[card[1]] != colour:
            return None
    index = 1
    while index < 4:
        try:
            if current_card + 1 == int(valuedict[naturals[index][0]]):
                outputgroup.append(naturals[index])
                current_card += 1
                index += 1
            elif aces != []:
                outputgroup.append(aces[0])
                current_card += 1
                aces.remove(aces[0])
            else:
                break
        except IndexError:
            if aces != []:
                outputgroup.append(aces[0])
                current_card += 1
                aces.remove(aces[0])
            else:
                break

    if outputgroup[0][0] == "A":
        increase = 1
        for index in range(1, len(outputgroup)):
            if outputgroup[index][0] != "A":
                current_ace = (int(valuedict[outputgroup[index][0]]) -
                               increase)
                if current_ace <= 1:
                    valid = False
                break
            increase += 1

    if outputgroup[-1][0] == "A":
        increase = 0
        for index in reversed(range(len(outputgroup))):
            if outputgroup[index][0] != "A":
                current_ace = (int(valuedict[outputgroup[index][0]]) +
                               increase)
                if current_ace >= 14:
                    valid = False
                break
            increase += 1

    if valid is True and len(outputgroup) == 4:
        return outputgroup
    else:
        return None


def phasedout_play(player_id, table, turn_history, phase_status,
                   hand, discard):
    """ Determine the best move that can be played in the game "Phased Out" by
    considering the contents of the table, turn_history, phase_status, hand and
    discard. The best move for each phase on how to draw and discard are also
    considered
    """
    try:
        last_move = turn_history[-1][-1][-1][0]
    except IndexError:
        last_move = None
    play = None
    my_phase = phase_status[player_id]

    # Condition to draw a card from deck/discard pile.

    if last_move == 5 or last_move is None:
        # Condition if player hasn't played the phase this round.
        if table[player_id][0] is None:

            # Target phase: phase 1. Draw card from discard pile if it
            # forms a 3 of a kind.
            if my_phase == 0:
                occurrences = defaultdict(int)
                drawcards = []
                for card in hand:
                    occurrences[card[0]] += 1
                for numcard in occurrences.keys():
                    if occurrences[numcard] == 2 and numcard != "A":
                        drawcards.append(numcard)
                # Only maximimum of 2 aces are needed to complete phase 1.
                if occurrences["A"] < 2:
                    drawcards.append('A')
                if discard[0] in drawcards:
                    play = (2, discard)
                    return play
                else:
                    play = (1, None)
                    return play

            # Target phase: phase 2. Draw card from discard pile if it is
            # the same suit as the suit with the most cards in the hand.
            elif my_phase == 1:
                occurrences = defaultdict(int)
                drawcard = None
                for card in hand:
                    occurrences[card[1]] += 1
                drawcard = max(occurrences, key=lambda i: occurrences[i])
                if discard[1] == drawcard or discard[0] == "A":
                    play = (2, discard)
                    return play
                else:
                    play = (1, None)
                    return play

            # Target phase: phase 3. Draw card from discard pile if it forms
            # a 4 of a kind.
            elif my_phase == 2:
                occurrences = defaultdict(int)
                drawcards = []
                pairs = []
                triple = []
                for card in hand:
                    occurrences[card[0]] += 1
                for numcard in occurrences.keys():
                    if occurrences[numcard] == 2:
                        pairs.append(numcard)
                    if occurrences[numcard] == 3:
                        triple.append(numcard)
                values = ["A", "2", "3", "4", "5", "6", "7", "8", "9",
                          "0", "J", "Q", "K"]
                pairs.sort(key=lambda c: values.index(c[0]), reverse = True)
                triple.sort(key=lambda c: values.index(c[0]), reverse = True)

                # Conditions to draw from discard pile depends on how many
                # triples and pairs in hand. Sort and take the lowest possible
                # pairs and triples from the discard pile. (Since only 2 4 of
                # a kinds are required)
                if len(triple) >= 2:
                    drawcards.append(triple[-1])
                    drawcards.append(triple[-2])
                elif len(triple) == 1 and len(pairs) >= 1:
                    drawcards.append(triple[0])
                    drawcards.append(pairs[-1])
                elif len(triple) == 1 and len(pairs) == 0:
                    drawcards.append(triple[0])
                elif len(triple) == 0 and len(pairs) >= 2:
                    drawcards.append(pairs[-1])
                    drawcards.append(pairs[-2])
                elif len(triple) == 0 and len(pairs) == 1:
                    drawcards.append(pairs[0])

                # Maximum of 4 aces are required to complete phase 2.
                if occurrences['A'] <= 4:
                    drawcards.append('A')
                if discard[0] in drawcards:
                    play = (2, discard)
                    return play
                else:
                    play = (1, None)
                    return play

            # Target phase: phase 4. Draw card from discard pile if the card
            # of a particular value is not in the hand.
            elif my_phase == 3:
                carddict = {"2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0,
                            "8": 0, "9": 0, "0": 0, "J": 0, "Q": 0, "K": 0}
                drawcards = []
                for card in hand:
                    if card[0] == "A":
                        pass
                    else:
                        carddict[card[0]] += 1
                for numcard in carddict.keys():
                    if carddict[numcard] == 0:
                        drawcards.append(numcard)
                drawcards.append("A")
                if discard[0] in drawcards:
                    play = (2, discard)
                    return play
                else:
                    play = (1, None)
                    return play

            # Target phase: phase 5. Draw card from discard pile if it forms
            # either a 4 of a kind or the same colour.
            elif my_phase == 4:
                pairs = []
                triple = []
                suitdict = {"C": "B", "S": "B", "D": "R", "H": "R"}
                # drawcards refer to a list of possible cards to draw from
                # triples or pairs.
                drawcards = []
                colouroccurrences = defaultdict(int)
                occurrences = defaultdict(int)
                for card in hand:
                    colouroccurrences[suitdict[card[1]]] += 1
                    occurrences[card[0]] += 1
                for numcard in occurrences.keys():
                    if occurrences[numcard] == 2:
                        pairs.append(numcard)
                    if occurrences[numcard] == 3:
                        triple.append(numcard)
                values = ["A", "2", "3", "4", "5", "6", "7", "8", "9",
                          "0", "J", "Q", "K"]
                pairs.sort(key = lambda c: values.index(c[0]), reverse = True)
                triple.sort(key = lambda c: values.index(c[0]), reverse = True)
                # Check how many triples and pairs in hand. Only 2 4 of a
                # kinds are needed to complete the phase.
                if len(triple) >= 2:
                    drawcards.append(triple[-1])
                    drawcards.append(triple[-2])
                elif len(triple) == 1 and len(pairs) >= 1:
                    drawcards.append(triple[0])
                    drawcards.append(pairs[-1])
                drawcards.append("A")
                # drawcard refers to the most dominant colour in the hand.
                drawcard = (max(colouroccurrences, key = lambda
                            i: occurrences[i]))
                if (suitdict[discard[1]] == drawcard and discard[0] <= "9" or
                        discard[0] in drawcards):
                    play = (2, discard)
                    return play
                else:
                    play = (1, None)
                    return play

        # Condition if a phase has been played this round.
        else:
            # Implement a function to check if card from discard pile can
            # be placed to a phase on the table.
            valid = check_placeable(table, discard)
            if valid is True:
                play = (2, discard)
                return play
            else:
                play = (1, None)
                return play

    # If card has been drawn this round:
    else:
        # Condition if a phase has been played this round,
        # attempt to discard cards to other players' phases.
        if table[player_id][0] is not None:
            # Check all cards in hand, this is assigned as card2.
            for card2 in hand:
                # Check all player tables and their phase type.
                for index in range(len(table)):

                    # Condition where player's table is empty.
                    if table[index][0] is None:
                        pass

                    # Condition where player's table has phase 1 or 3.
                    elif table[index][0] == 1 or table[index][0] == 3:
                        # Determine the value of the group, exclude Aces.
                        for card in table[index][1][0]:
                            if card[0] == "A":
                                pass
                            else:
                                if card[0] == card2[0] or card2[0] == "A":
                                    play = ((4, (card2, (index, 0,
                                            len(table[index][1][0])))))
                                    return play
                                else:
                                    break
                        for card in table[index][1][1]:
                            if card[0] == "A":
                                pass
                            else:
                                if card[0] == card2[0] or card2[0] == "A":
                                    play = ((4, (card2, (index, 1,
                                            len(table[index][1][1])))))
                                    return play
                                else:
                                    break

                    # Condition where player's table has phase 2.
                    elif table[index][0] == 2:
                        # Determine if card2 has the same suit as the table.
                        # Exclude Aces.
                        for card in table[index][1]:
                            if card[0] == "A":
                                pass
                            else:
                                if card[1] == card2[1] or card2[0] == "A":
                                    play = ((4, (card2, (index, 0,
                                            len(table[index][1][0])))))
                                    return play
                                else:
                                    break

                    # Condition where player's table has phase 4.
                    elif table[index][0] == 4:
                        numlist = []
                        valuedict = {"2": "2", "3": "3", "4": "4", "5": "5",
                                     "6": "6", "7": "7", "8": "8", "9": "9",
                                     "0": "10", "J": "11", "Q": "12",
                                     "K": "13", "A": "25"}
                        # Determine the value of each card in the run.
                        for cards in table[index][1][0]:
                            if cards[0] == "A":
                                numlist.append("A")
                            else:
                                numlist.append(valuedict[cards[0]])

                        current_card = valuedict[card2[0]]
                        first_card_num = numlist[0]
                        last_card_num = numlist[-1]

                        # Check the value of the first and last cards
                        if first_card_num == "A":
                            decrease = 0
                            for number in numlist:
                                if number != "A":
                                    first_card_num = int(number) - decrease
                                decrease += 1

                        if last_card_num == "A":
                            increase = 0
                            for number in reversed(numlist):
                                if number != "A":
                                    last_card_num = int(number) + increase
                                    break
                                increase += 1

                        # If an ace is to be played. Check whether placing
                        # at either ends of the run will satisfy the run value.
                        if card2[0] == "A":
                            if last_card_num == "13" or last_card_num == 13:
                                pass
                            else:
                                play = ((4, (card2, (index, 0,
                                        len(table[index][1][0])))))
                                return play
                            if first_card_num == "2" or first_card_num == 2:
                                pass
                            else:
                                play = (4, (card2, (index, 0, 0)))
                                return play

                        # Check whether playing a card will satisfy the run.
                        elif int(current_card) == int(last_card_num) + 1:
                            play = ((4, (card2, (index, 0,
                                    len(table[index][1][0])))))
                            return play

                        elif int(current_card) == int(first_card_num) - 1:
                            play = (4, (card2, (index, 0, 0)))
                            return play

                    # Condition where player's table has phase 5
                    elif table[index][0] == 5:
                        # Similar concept to phase 4, but consider colour.
                        numlist = []
                        suitdict = {"S": "B", "C": "B", "D": "R", "H": "R"}
                        colour = None
                        cardcolour = suitdict[card2[1]]
                        valuedict = {"2": "2", "3": "3", "4": "4", "5": "5",
                                     "6": "6", "7": "7", "8": "8", "9": "9",
                                     "0": "10", "J": "11", "Q": "12",
                                     "K": "13", "A": "25"}
                        # Determine colour of the run, exclude Aces.
                        for card in table[index][1][0]:
                            if card[0] == "A":
                                pass
                            else:
                                colour = suitdict[card[1]]
                                break
                        # Determine values of each card.
                        for card in table[index][1][0]:
                            if card[0] == "A":
                                numlist.append("A")
                            else:
                                numlist.append(valuedict[card[0]])

                        current_card = valuedict[card2[0]]
                        first_card_num = numlist[0]
                        last_card_num = numlist[-1]

                        if first_card_num == "A":
                            decrease = 0
                            for number in numlist:
                                if number != "A":
                                    first_card_num = int(number) - decrease
                                    break
                                decrease += 1

                        if last_card_num == "A":
                            increase = 0
                            for number in reversed(numlist):
                                if number != "A":
                                    last_card_num = int(number) + increase
                                    break
                                increase += 1

                        if card2[0] == "A":
                            if last_card_num == "13" or last_card_num == 13:
                                pass
                            else:
                                play = ((4, (card2, (index, 0,
                                        len(table[index][1][0])))))
                                return play
                            if first_card_num == "2" or first_card_num == 2:
                                pass
                            else:
                                play = (4, (card2, (index, 0, 0)))
                                return play

                        # Similar condition to phase 4, but colour must match.
                        else:
                            if (int(current_card) == int(last_card_num) + 1 and
                                    cardcolour == colour):
                                play = ((4, (card2, (index, 0,
                                        len(table[index][1][0])))))
                                return play
                            elif (int(current_card) == int(first_card_num) -
                                    1 and cardcolour == colour):
                                play = (4, (card2, (index, 0, 0)))
                                return play
                            else:
                                pass

                        # For the second group in the table, which is group 3.
                        # Similar conditions to phase 1 and 3 checks.
                        for card in table[index][1][1]:
                            if card[0] == "A":
                                pass
                            else:
                                if card[0] == card2[0] or card2[0] == "A":
                                    play = ((4, (card2, (index, 1,
                                            len(table[index][1][1])))))
                                    return play
                                else:
                                    pass
        else:
            # Attempt to form a phase if player's table is empty.
            # Attempt to find combinations for phase 1
            if my_phase == 0:
                grouplist = []
                for handcombination in combinations(hand, 3):
                    group1 = check_group1(handcombination)
                    if group1 is True:
                        grouplist.append(handcombination)

                # Repeat for all possible group 1s and check if play is valid.
                for handcombination in combinations(grouplist, 2):
                    valid = True
                    combination = handcombination[0] + handcombination[1]
                    backup_hand = list(hand)
                    # Check whether the two combinations collide with hand.
                    # Prevent any duplicates.
                    for card in combination:
                        if card not in backup_hand:
                            valid = False
                            break
                        else:
                            backup_hand.remove(card)
                    if valid is True:
                        play = ((3, [list(handcombination[0]),
                                list(handcombination[1])]))
                        return play

            # Attempt to find combinations for phase 2.
            elif my_phase == 1:
                for handcombination in combinations(hand, 7):
                    group2 = check_group2(handcombination)
                    if group2 is True:
                        play = (3, [list(handcombination)])
                        return play
                    else:
                        pass

            # Attempt to find combinations for phase 3
            elif my_phase == 2:
                grouplist = []
                for handcombination in combinations(hand, 4):
                    group3 = check_group3(handcombination)
                    if group3 is True:
                        grouplist.append(handcombination)

                # Similar to phase 1, determine whether combination will
                # collide with the hand and prevent duplicates.
                for handcombination in combinations(grouplist, 2):
                    valid = True
                    combination = handcombination[0] + handcombination[1]
                    backup_hand = list(hand)
                    for card in combination:
                        if card not in backup_hand:
                            valid = False
                            break
                        else:
                            backup_hand.remove(card)
                    if valid is True:
                        play = ((3, [list(handcombination[0]),
                                list(handcombination[1])]))
                        return play

            # Since permutation is not valid for phase 4 (long processing time)
            # perform sorted combination.
            elif my_phase == 3:
                values = ["2", "3", "4", "5", "6", "7", "8", "9",
                          "0", "J", "Q", "K", "A"]
                hand.sort(key = lambda c: values.index(c[0]))
                for handcombination in combinations(hand, 8):
                    # check_group4 will attempt to place the aces in the
                    # proper order and check if group 4 is valid.
                    group4 = check_group4(handcombination)
                    if group4 is not None:
                        play = (3, [list(group4)])
                        return play

            # For phase 5, attempt to find combinations for group 3 and
            # sorted combination for group 5.
            elif my_phase == 4:
                grouplist = []
                grouplist2 = []
                values = ["2", "3", "4", "5", "6", "7", "8", "9",
                          "0", "J", "Q", "K", "A"]
                hand.sort(key = lambda c: values.index(c[0]))
                for handcombination in combinations(hand, 4):
                    # check_group5 will place aces in the proper order as
                    # necessary and check if group 5 is valid.
                    group5 = check_group5(handcombination)
                    if group5 is not None:
                        grouplist.append(list(group5))
                for handcombination in combinations(hand, 4):
                    group3 = check_group3(handcombination)
                    if group3 is True:
                        grouplist2.append(list(handcombination))

                # Prevent duplicates and collision to hand.
                for firstgroup in grouplist:
                    for secondgroup in grouplist2:
                        valid = True
                        totalgroup = firstgroup + secondgroup
                        backup_hand = list(hand)
                        for card in totalgroup:
                            if card not in backup_hand:
                                valid = False
                                break
                            else:
                                backup_hand.remove(card)
                        if valid is True:
                            play = (3, [list(firstgroup), list(secondgroup)])
                            return play

    # This is to discard a card to the discard pile. Check whether a phase
    # has been played or not this round.
    if table[player_id][0] is None:
        # To satisfy phase 1. Idea is to throw the highest valued card that
        # does not have a pair.
        if my_phase == 0:
            occurrences = defaultdict(int)
            discards = []
            for card in hand:
                occurrences[card[0]] += 1
            for numcard in occurrences.keys():
                if occurrences[numcard] == 1:
                    discards.append(numcard)
            values = ["A", "2", "3", "4", "5", "6", "7", "8", "9",
                      "0", "J", "Q", "K"]
            hand.sort(key = lambda c: values.index(c[0]), reverse = True)
            for card in hand:
                # Sort hand, and prevent Ace from being discarded.
                if card[0] in discards and card[0] != "A":
                    play = (5, card)
                    return play
            # As the last resort, discard the highest valued card in the hand.
            # The same applies to other phase conditions.
            play = (5, hand[0])
            return play

        # To satisfy phase 2. Idea is to throw the highest valued card that
        # isn't the most dominant suit.
        elif my_phase == 1:
            occurrences = defaultdict(int)
            for card in hand:
                occurrences[card[1]] += 1
            values = ["A", "2", "3", "4", "5", "6", "7", "8", "9",
                      "0", "J", "Q", "K"]
            hand.sort(key = lambda c: values.index(c[0]), reverse = True)
            # Find the suit that is the most dominant in hand. Prevent those
            # cards from being discarded.
            keepcard = max(occurrences, key = lambda i: occurrences[i])
            for card in hand:
                if card[1] != keepcard and card[0] != "A":
                    play = (5, card)
                    return play
            play = (5, hand[0])
            return play

        # To satisfy phase 3. Idea is to throw highest value cards that does
        # not have a pair.
        elif my_phase == 2:
            occurrences = defaultdict(int)
            discards = []
            for card in hand:
                occurrences[card[0]] += 1
            for numcard in occurrences.keys():
                if occurrences[numcard] == 1 or occurrences[numcard] > 4:
                    discards.append(numcard)
            values = ["A", "2", "3", "4", "5", "6", "7", "8", "9",
                      "0", "J", "Q", "K"]
            hand.sort(key = lambda c: values.index(c[0]), reverse = True)
            for card in hand:
                if card[0] in discards and card[0] != "A":
                    play = (5, card)
                    return play
            play = (5, hand[0])
            return play

        # To satisfy phase 4. Idea is to find the highest cards that has more
        # than 1 card of the same value in the hand.
        elif my_phase == 3:
            occurrences = defaultdict(int)
            discards = []
            for card in hand:
                occurrences[card[0]] += 1
            for numcard in occurrences.keys():
                if occurrences[numcard] > 1:
                    discards.append(numcard)
            values = ["A", "2", "3", "4", "5", "6", "7", "8", "9",
                      "0", "J", "Q", "K"]
            hand.sort(key = lambda c: values.index(c[0]), reverse = True)
            for card in hand:
                if card[0] in discards:
                    play = (5, card)
                    return play
            play = (5, hand[0])
            return play

        # To satisfy phase 5. Idea is to keep cards that satisfies group 5 or 3
        # and possible triples that can form group 3.
        elif my_phase == 4:
            # keeptriple is not a dictionary since only 1 triple is required
            # that can be aimed for 4 of a kind.
            keepcards = []
            keeptriple = None
            occurrences = defaultdict(int)
            for card in hand:
                occurrences[card[0]] += 1
            for numcard in occurrences.keys():
                if occurrences[numcard] == 3:
                    keeptriple = numcard
            values = ["A", "2", "3", "4", "5", "6", "7", "8", "9",
                      "0", "J", "Q", "K"]
            hand.sort(key = lambda c: values.index(c[0]))
            # Check whether cards in the hand has satisfied either group 5 or 3
            for handcombination in combinations(hand, 4):
                group5 = check_group5(handcombination)
                if group5 is not None:
                    for card in group5:
                        keepcards.append(card)
                        break
            for handcombination in combinations(hand, 4):
                group3 = check_group3(handcombination)
                if group3 is True:
                    for card in handcombination:
                        keepcards.append(card)
                        break
            values = ["A", "2", "3", "4", "5", "6", "7", "8", "9",
                      "0", "J", "Q", "K"]
            # Throw highest card that does not satisfy groups 5 or 3.
            hand.sort(key = lambda c: values.index(c[0]), reverse = True)
            for card in hand:
                if card in keepcards or card[0] == keeptriple:
                    pass
                else:
                    play = (5, card)
                    return play
            play = (5, hand[0])
            return play

    # Condition where a phase has been played. Throw the highest valued card
    # in the hand.
    else:
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9",
                  "0", "J", "Q", "K"]
        hand.sort(key = lambda c: values.index(c[0]), reverse = True)
        play = (5, hand[0])
        return play


def check_placeable(table, card2):
    """ check_placeable function checks whether a card from the discard pile
    can be played to a phase on the table. (Only valid when a phase has been
    played this round) Function is the same as checking whether placing a card
    is valid.
    """
    valid = False
    for index in range(len(table)):
        if table[index][0] is None:
            pass
        elif table[index][0] == 1 or table[index][0] == 3:
            for card in table[index][1][0]:
                if card[0] == "A":
                    pass
                else:
                    if card[0] == card2[0] or card2[0] == "A":
                        valid = True
                    else:
                        break
            for card in table[index][1][1]:
                if card[0] == "A":
                    pass
                else:
                    if card[0] == card2[0] or card2[0] == "A":
                        valid = True
                    else:
                        break
        elif table[index][0] == 2:
            for card in table[index][1]:
                if card[0] == "A":
                    pass
                else:
                    if card[1] == card2[1] or card2[0] == "A":
                        valid = True
                    else:
                        break
        elif table[index][0] == 4:
            numlist = []
            valuedict = {"2": "2", "3": "3", "4": "4", "5": "5",
                         "6": "6", "7": "7", "8": "8", "9": "9",
                         "0": "10", "J": "11", "Q": "12",
                         "K": "13", "A": "25"}

            for cards in table[index][1][0]:
                if cards[0] == "A":
                    numlist.append("A")
                else:
                    numlist.append(valuedict[cards[0]])

            current_card = valuedict[card2[0]]
            first_card_num = numlist[0]
            last_card_num = numlist[-1]

            if first_card_num == "A":
                decrease = 0
                for number in numlist:
                    if number != "A":
                        first_card_num = int(number) - decrease
                    decrease += 1

            if last_card_num == "A":
                increase = 0
                for number in reversed(numlist):
                    if number != "A":
                        last_card_num = int(number) + increase
                        break
                    increase += 1

            if card2[0] == "A":
                if last_card_num == "13" or last_card_num == 13:
                    pass
                else:
                    valid = True
                if first_card_num == "2" or first_card_num == 2:
                    pass
                else:
                    valid = True

            elif int(current_card) == int(last_card_num) + 1:
                valid = True

            elif int(current_card) == int(first_card_num) - 1:
                valid = True

        elif table[index][0] == 5:
            numlist = []
            suitdict = {"S": "B", "C": "B", "D": "R", "H": "R"}
            colour = None
            cardcolour = suitdict[card2[1]]
            valuedict = {"2": "2", "3": "3", "4": "4", "5": "5",
                         "6": "6", "7": "7", "8": "8", "9": "9",
                         "0": "10", "J": "11", "Q": "12",
                         "K": "13", "A": "25"}

            for card in table[index][1][0]:
                if card[0] == "A":
                    pass
                else:
                    colour = suitdict[card[1]]
                    break
            for card in table[index][1][0]:
                if card[0] == "A":
                    numlist.append("A")
                else:
                    numlist.append(valuedict[card[0]])

            current_card = valuedict[card2[0]]
            first_card_num = numlist[0]
            last_card_num = numlist[-1]

            if first_card_num == "A":
                decrease = 0
                for number in numlist:
                    if number != "A":
                        first_card_num = int(number) - decrease
                        break
                    decrease += 1

            if last_card_num == "A":
                increase = 0
                for number in reversed(numlist):
                    if number != "A":
                        last_card_num = int(number) + increase
                        break
                    increase += 1

            if card2[0] == "A":
                if last_card_num == "13" or last_card_num == 13:
                    pass
                else:
                    valid = True
                if first_card_num == "2" or first_card_num == 2:
                    pass
                else:
                    valid = True

            else:
                if (int(current_card) == int(last_card_num) + 1 and
                        cardcolour == colour):
                    valid = True
                elif (int(current_card) == int(first_card_num) - 1 and
                        cardcolour == colour):
                    valid = True
                else:
                    pass

            for card in table[index][1][1]:
                if card[0] == "A":
                    pass
                else:
                    if card[0] == card2[0] or card2[0] == "A":
                        valid = True
                    else:
                        pass

    return valid
