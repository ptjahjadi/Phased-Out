from itertools import combinations
from collections import defaultdict

# There are 5 functions to check validity of each group, similar to Q1.
# For each of these 5 functions, return False if Joker is in the combination.


def check_group1(group):
    """ This function checks the validity of group 1 in the combination
    of cards. This function acts similar to Q1 with less considerations and
    only focusing in group 1 validity.
    """
    if "ZZ" in group:
        return False
    else:
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
    if "ZZ" in group:
        return False
    else:
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
    if "ZZ" in group:
        return False
    else:
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
    if "ZZ" in group:
        return None
    else:
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
        # current_card refers to the value of the card currently, useful in 
        #a loop later on.
        current_card = int(valuedict[naturals[0][0]])
        index = 1
        # The loop will put Ace wherever necessary in attempt to
        # satisfy the run.
        while index < 8:
            # while index < 8 assumes that all the cards are natural cards. 
            # In the case of the naturals list being exhausted, perform 
            # exception handling to consider only aces.
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


def check_group5(group):
    """ This function checks the validity of group 5 in the combination
    of cards. This function acts similar to Q1 with less considerations and
    only focusing in group 5 validity. Moreover, the placement of Aces are
    considered here and the correct hand formation from the sorted combinations
    are formed.
    """
    if "ZZ" in group:
        return None
    else:
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
        # Check whether all natural cards adhere to the same colour.
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


def phasedout_bonus(player_id, table, turn_history, phase_status,
                    hand, discard):
    """ Determine the best move that can be played in the bonus game
    "Phased Out" with the addition of jokers and phase considerations
    considering the contents of the table, turn_history, phase_status, hand and
    discard. The best move for each phase on how to draw and discard are also
    considered along with the best phase that can be played that round.
    """
    try:
        last_move = turn_history[-1][-1][-1][0]
        play = None
    except IndexError:
        last_move = None
        play = None

    # Determine target phase for the round by considering phases that have been
    # completed and have not.
    complete_phase = []
    incomplete_phase = []
    for phase in range(0, 5):
        if phase_status[player_id][phase] is not False:
            complete_phase.append(phase + 1)
        else:
            incomplete_phase.append(phase + 1)
    numoccurrences = defaultdict(int)
    suitoccurrences = defaultdict(int)
    # pairlist and triplelist are useful to store pairs and triples to
    # consider phase 1 or 3. ones are useful to consider phase 4, where the
    # less pairs/triples there are, the better.
    pairlist = []
    triplelist = []
    ones = 0
    for card in hand:
        numoccurrences[card[0]] += 1
        suitoccurrences[card[1]] += 1
    # Determine the suit that is most dominant in the hand.
    maxsuit = max(suitoccurrences, key = lambda i: suitoccurrences[i])
    for number in numoccurrences.keys():
        if numoccurrences[number] > 1:
            pairlist.append(number)
        if numoccurrences[number] > 2:
            triplelist.append(number)
        if numoccurrences[number] == 1:
            ones += 1

    # Here are list of priorities to consider each phase, with the lowest
    # priority in the bottom, depending on the hand.
    if maxsuit > "3" and 2 not in complete_phase:
        target_phase = 2
    elif len(triplelist) >= 2 and 3 not in complete_phase:
        target_phase = 3
    elif ones > 5 and 4 not in complete_phase:
        target_phase = 4
    elif len(triplelist) >= 1 and 1 not in complete_phase:
        target_phase = 1
    elif len(pairlist) >= 2 and 1 not in complete_phase:
        target_phase = 1
    elif ones > 4 and 4 not in complete_phase:
        target_phase = 4
    elif maxsuit > "2" and 2 not in complete_phase:
        target_phase = 2
    elif len(pairlist) >= 2 and 3 not in complete_phase:
        target_phase = 3
    elif 1 not in complete_phase:
        target_phase = 1
    elif 2 not in complete_phase:
        target_phase = 2
    elif 3 not in complete_phase:
        target_phase = 3
    elif 4 not in complete_phase:
        target_phase = 4
    elif 5 not in complete_phase:
        target_phase = 5

    # Condition to draw a card from deck/discard pile.
    if last_move == 5 or last_move == 6 or last_move is None:
        # Condition if a phase hasn't been played.
        # Conditions are all the same with phasedout_play.
        if table[player_id] is None:
            if target_phase == 1:
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

            elif target_phase == 2:
                occurrences = defaultdict(int)
                drawcard = None
                for card in hand:
                    occurrences[card[1]] += 1
                drawcard = max(occurrences, key = lambda i: occurrences[i])
                if discard[1] == drawcard or discard[0] == "A":
                    play = (2, discard)
                    return play
                else:
                    play = (1, None)
                    return play

            elif target_phase == 3:
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
                pairs.sort(key = lambda c: values.index(c[0]), reverse = True)
                triple.sort(key = lambda c: values.index(c[0]), reverse = True)

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

                # Maximum of 4 aces are required to complete phase 4.
                if occurrences['A'] <= 4:
                    drawcards.append('A')
                if discard[0] in drawcards:
                    play = (2, discard)
                    return play
                else:
                    play = (1, None)
                    return play

            elif target_phase == 4:
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

            elif target_phase == 5:
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

    else:
        # Condition if it's the same round as the phase is played,
        # attempt to discard cards to other players' phases.
        if table[player_id][0] is not None:
            for card2 in hand:
                # Jokers cannot be played to another phase.
                if card2 == "ZZ":
                    pass
                else:
                    # Conditions are the same as phasedout_play.
                    for index in range(len(table)):
                        if table[index][0] is None:
                            pass
                        elif table[index][0] == 1 or table[index][0] == 3:
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
                        elif table[index][0] == 2:
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
                        elif table[index][0] == 4:
                            numlist = []
                            for cards in table[index][1][0]:
                                if cards[0] == "0":
                                    numlist.append("10")
                                elif cards[0] == "J":
                                    numlist.append("11")
                                elif cards[0] == "Q":
                                    numlist.append("12")
                                elif cards[0] == "K":
                                    numlist.append("13")
                                else:
                                    numlist.append(cards[0])
                            current_card = None
                            if card2[0] == "2":
                                current_card = "2"
                            elif card2[0] == "3":
                                current_card = "3"
                            elif card2[0] == "4":
                                current_card = "4"
                            elif card2[0] == "5":
                                current_card = "5"
                            elif card2[0] == "6":
                                current_card = "6"
                            elif card2[0] == "7":
                                current_card = "7"
                            elif card2[0] == "8":
                                current_card = "8"
                            elif card2[0] == "9":
                                current_card = "9"
                            elif card2[0] == "0":
                                current_card = "10"
                            elif card2[0] == "J":
                                current_card = "11"
                            elif card2[0] == "Q":
                                current_card = "12"
                            elif card2[0] == "K":
                                current_card = "13"
                            elif card2[0] == "A":
                                current_card = "25"

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
                                if (last_card_num == "13" or
                                        last_card_num == 13):
                                    pass
                                else:
                                    play = ((4, (card2, (index, 0,
                                            len(table[index][1][0])))))
                                    return play
                                if (first_card_num == "2" or
                                        first_card_num == 2):
                                    pass
                                else:
                                    play = (4, (card2, (index, 0, 0)))
                                    return play

                            elif int(current_card) == int(last_card_num) + 1:
                                if (last_card_num == "13" or
                                        last_card_num == 13):
                                    pass
                                else:
                                    play = ((4, (card2, (index, 0,
                                            len(table[index][1][0])))))
                                    return play

                            elif int(current_card) == int(first_card_num) - 1:
                                if (first_card_num == "2" or
                                        first_card_num == 2):
                                    pass
                                else:
                                    play = (4, (card2, (index, 0, 0)))
                                    return play

                        elif table[index][0] == 5:
                            numlist = []
                            suitdict = {"S": "B", "C": "B", "D": "R", "H": "R"}
                            colour = None
                            cardcolour = suitdict[card2[1]]
                            for card in table[index][1][0]:
                                if card[0] == "A":
                                    pass
                                else:
                                    colour = suitdict[card[1]]
                                    break
                            for card in table[index][1][0]:
                                if card[0] == "0":
                                    numlist.append("10")
                                elif card[0] == "J":
                                    numlist.append("11")
                                elif card[0] == "Q":
                                    numlist.append("12")
                                elif card[0] == "K":
                                    numlist.append("13")
                                else:
                                    numlist.append(card[0])
                            current_card = None
                            if card2[0] == "2":
                                current_card = "2"
                            elif card2[0] == "3":
                                current_card = "3"
                            elif card2[0] == "4":
                                current_card = "4"
                            elif card2[0] == "5":
                                current_card = "5"
                            elif card2[0] == "6":
                                current_card = "6"
                            elif card2[0] == "7":
                                current_card = "7"
                            elif card2[0] == "8":
                                current_card = "8"
                            elif card2[0] == "9":
                                current_card = "9"
                            elif card2[0] == "0":
                                current_card = "10"
                            elif card2[0] == "J":
                                current_card = "11"
                            elif card2[0] == "Q":
                                current_card = "12"
                            elif card2[0] == "K":
                                current_card = "13"
                            elif card2[0] == "A":
                                current_card = "25"

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
                                if (last_card_num == "13" or
                                        last_card_num == 13):
                                    pass
                                else:
                                    play = ((4, (card2, (index, 0,
                                            len(table[index][1][0])))))
                                    return play
                                if (first_card_num == "2" or
                                        first_card_num == 2):
                                    pass
                                else:
                                    play = (4, (card2, (index, 0, 0)))
                                    return play

                            else:
                                if (int(current_card) ==
                                        int(last_card_num) + 1 and
                                        cardcolour == colour):
                                    play = ((4, (card2, (index, 0,
                                            len(table[index][1][0])))))
                                    return play
                                elif (int(current_card) ==
                                      int(first_card_num) - 1 and
                                      cardcolour == colour):
                                    play = (4, (card2, (index, 0, 0)))
                                    return play
                                else:
                                    pass

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
            # Depending on the target_phase, attempt to form a phase similar
            # to phasedout_play
            # Find best move to satisfy phase 1
            if target_phase == 1:
                grouplist = []
                # Attempt to find combinations for phase 1
                for handcombination in combinations(hand, 3):
                    group1 = check_group1(handcombination)
                    if group1 is True:
                        grouplist.append(handcombination)
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

            # Attempt to find combinations for phase 2.
            elif target_phase == 2:
                for handcombination in combinations(hand, 7):
                    group2 = check_group2(handcombination)
                    if group2 is True:
                        play = (3, [list(handcombination)])
                        return play
                    else:
                        pass

            elif target_phase == 3:
                grouplist = []
                # Attempt to find combinations for phase 3.
                for handcombination in combinations(hand, 4):
                    group3 = check_group3(handcombination)
                    if group3 is True:
                        grouplist.append(handcombination)
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

            elif target_phase == 4:
                values = ["2", "3", "4", "5", "6", "7", "8", "9",
                          "0", "J", "Q", "K", "A", "Z"]
                hand.sort(key = lambda c: values.index(c[0]))
                for handcombination in combinations(hand, 8):
                    # check_group4 will attempt to place the aces in the
                    # proper order and check if group 4 is valid.
                    group4 = check_group4(handcombination)
                    if group4 is not None:
                        play = (3, [list(group4)])
                        return play

            elif target_phase == 5:
                grouplist = []
                grouplist2 = []
                values = ["2", "3", "4", "5", "6", "7", "8", "9",
                          "0", "J", "Q", "K", "A", "Z"]
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

    # This is to discard a card to the discard pile.
    # Prioritise discarding the Joker since it has no use in forming a phase.
    if 'ZZ' in hand:
        if player_id == 3:
            play = (6, 0)
            return play
        else:
            play = (6, player_id + 1)
            return play
    # Conditions where there are no more Jokers in hand, conditions are the
    # same as phasedout_play.
    elif table[player_id][0] is None:
        if target_phase == 1:
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

        elif target_phase == 2:
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

        elif target_phase == 3:
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

        elif target_phase == 4:
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

        elif target_phase == 5:
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
    if card2 == "ZZ":
        return False
    else:
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
