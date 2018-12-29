# Use the same function as Q1.


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
    # Find the first suit that is not an ace to be compared in check_Suit
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
                # in the case of ace valuing 1 or lower, nullify group 4/5
                if current_ace == 1:
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
                    # in the case of ace valuing 14 or higher, negate group 4/5
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
        # (the previous card)
        elif numberlist[check_straight-1] == "A":
            if current_ace == int(numberlist[check_straight]) - 1:
                straight_count += 1
            else:
                break
        # Check whether the run continues
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

# Implement Q2.


def phasedout_phase_type(phase):
    """ Determine the phase type of the groups formed for the game "Phase Out".
    The function will be referred from phasedout_group_type and the combination
    of card groups will be used to determine the phase
    """
    phaselist = []
    # Include repetition to determine each group's category.
    for group in phase:
        phaselist.append(phasedout_group_type(group))
    if phaselist == [1, 1]:
        return 1
    elif phaselist == [2]:
        return 2
    elif phaselist == [3, 3]:
        return 3
    elif phaselist == [4]:
        return 4
    elif phaselist == [5, 3]:
        return 5
    else:
        return None

# Implement Q3


def phasedout_is_valid_play(play, player_id, table, turn_history,
                            phase_status, hand, discard):
    """ Determine from the game "Phased Out" whether the move made by a player
    is valid or not. Consider the contents of the table, turn_history,
    phase_status, hand and discard.
    """
    # Determine the last play made by the previous player
    try:
        prev_player_turn = turn_history[-1][0]
        last_move = turn_history[-1][-1][-1][0]
    except IndexError:
        prev_player_turn = None
        last_move = 5

    # Determine whether or not it's the player's turn
    if player_id != prev_player_turn:
        if player_id != 0:
            if prev_player_turn != player_id + 1:
                return False
        elif player_id == 0:
            if prev_player_turn != 3:
                return False

    # Condition if the player wants to draw from the deck
    if play[0] == 1:
        # If the previous player hasn't discarded or the player has already
        # drawn, the player cannot draw
        if last_move != 5 or prev_player_turn == player_id:
            return False
        else:
            return True

    # Condition if the player wants to draw from the discard pile
    elif play[0] == 2:
        # If the previous player hasn't discarded or the player has already
        # drawn, or what is intended to draw is not in the top discard pile,
        # the player cannot draw
        if (last_move != 5 or play[1] != discard or
                prev_player_turn == player_id):
            return False
        else:
            return True

    # Condition if the player wants to place a phase
    elif play[0] == 3:
        # If the player hasn't drawn, the player cannot place a phase
        if last_move == 5:
            return False
        else:
            playlist = []
            # Exception handling in the case of 1 or 2 groups in the phase
            # Add to the cards that would like to be played for a phase
            try:
                playlist = play[1][0] + play[1][1]
            except IndexError:
                playlist = play[1][0]
            for card in playlist:
                if card not in hand:
                    return False
            phasetype = phasedout_phase_type(play[1])
            prev_phase = phase_status[player_id]
            # Check if the phase that the player wants to place is the next
            # required phase
            if prev_phase == phasetype - 1:
                return True
            else:
                return False

    # Condition if the player wants to place a card to others' phases
    elif play[0] == 4:
        # If the player hasn't drawn, the player cannot place a phase
        if last_move == 5:
            return False
        else:
            player_number = play[1][1][0]
            # If either the player or the designated player hasn't placed
            # a phase in that round, return False
            if table[player_id][0] is None or table[player_number][0] is None:
                return False
            else:
                # card refers to the players' card that wish to be played.
                # group_number determines which group the player wishes to play
                # group refers to the group content of the designated table
                card = play[1][0]
                group_number = play[1][1][1]
                index_position = play[1][1][2]
                player_table = table[player_number]
                group = player_table[1][group_number]
                if card not in hand:
                    return False

                # Conditions for phase 1 or 3. Idea is to find the card number
                # of the group (unless placing an Ace) while check if the index
                # position is valid
                if player_table[0] == 1 or player_table[0] == 3:
                    if card[0] == "A":
                        if (len(group) == index_position or
                                index_position == 0):
                            return True
                        else:
                            return False
                    elif card[0] != "A":
                        for card_num in player_table[1][group_number]:
                            if card_num[0] == "A":
                                pass
                            else:
                                cardnum = card_num
                                break
                        if (cardnum[0] == card[0] and
                            (len(group) == index_position or
                             index_position == 0)):
                            return True
                        else:
                            return False

                # Condition for phase 2. Idea is to find the suit of a non-Ace
                # card (unless placing an Ace) while check if the index
                # position is valid
                elif player_table[0] == 2:
                    for card_suit in group:
                        if card_suit[0] == "A":
                            pass
                        else:
                            suit = card_suit[1]
                            break
                    if suit == card[1] or card[0] == "A":
                        if len(group) == index_position or index_position == 0:
                            return True
                        else:
                            return False
                    else:
                        return False

                # Condition for phase 4. Idea is to find whether placing
                # a card at the beginning or end of the run would still
                # satisfy the run
                elif player_table[0] == 4:
                    numlist = []
                    # Determine the value of each card in the list
                    valuedict = {"2": "2", "3": "3", "4": "4", "5": "5",
                                 "6": "6", "7": "7", "8": "8", "9": "9",
                                 "0": "10", "J": "11", "Q": "12", "K": "13"}
                    for cards in player_table[1][0]:
                        if cards[0] == "A":
                            numlist.append("A")
                        else:
                            numlist.append(valuedict[cards[0]])

                    # Determine the numerical value of the card
                    if card[0] == "A":
                        pass
                    else:
                        card = valuedict[card[0]]

                    # Determine value of the first and last cards of the run.
                    # If they are aces, determine the value of those aces.
                    first_card_num = numlist[0]
                    last_card_num = numlist[-1]
                    if last_card_num == "A":
                        increase = 0
                        for number in reversed(numlist):
                            if number != "A":
                                last_card_num = int(number) + increase
                                break
                            increase += 1
                    if first_card_num == "A":
                        decrease = 0
                        for number in numlist:
                            if number != "A":
                                first_card_num = int(number) - decrease
                                break
                            decrease += 1

                    # Condition if the card placed is Ace, move is not valid
                    # if the last card is K or the first card is 2.
                    if card[0] == "A":
                        if len(group) == index_position:
                            if last_card_num == "13" or last_card_num == 13:
                                return False
                            else:
                                return True
                        elif index_position == 0:
                            if first_card_num == "2" or first_card_num == 2:
                                return False
                            else:
                                return True
                        else:
                            return False

                    # Conditions where the cards placed is either at the
                    # last index position or the first.
                    elif int(card) == int(last_card_num) + 1:
                        if last_card_num == "13" or last_card_num == 13:
                            return False
                        if len(group) == index_position:
                            return True
                        else:
                            return False

                    elif int(card) == int(first_card_num) - 1:
                        if first_card_num == "2" or first_card_num == 2:
                            return False
                        if index_position == 0:
                            return True
                        else:
                            return False
                    else:
                        return False

                # Conditions for phase 5. Check by group type.
                elif player_table[0] == 5:

                    # Similar condition check for phases 1 or 2
                    if group_number == 1:
                        cardnum = None
                        for card_num in group:
                            if card_num[0] == "A":
                                pass
                            else:
                                cardnum = card_num[0]
                                break
                        if cardnum == card[0] or card[0] == "A":
                            if (len(group) == index_position or
                                    index_position == 0):
                                return True
                            else:
                                return False
                        else:
                            return False

                    # Check for coloured run
                    elif group_number == 0:
                        if card[0] == "A" and len(group) == index_position:
                            return True
                        elif card[0] != "A":
                            numlist = []
                            suitdict = {"S": "B", "C": "B", "D": "R", "H": "R"}
                            cardcolour = suitdict[card[1]]
                            colour = None
                            valuedict = {"2": "2", "3": "3", "4": "4",
                                         "5": "5", "6": "6", "7": "7",
                                         "8": "8", "9": "9", "0": "10",
                                         "J": "11", "Q": "12", "K": "13"}

                            # Determine the colour of the run excluding Aces
                            for cards in player_table[1][0]:
                                if cards[0] == "A":
                                    pass
                                else:
                                    colour = suitdict[cards[1]]
                                    break
                            for cards in player_table[1][0]:
                                if cards[0] == "A":
                                    numlist.append("A")
                                else:
                                    numlist.append(valuedict[cards[0]])

                            if card[0] == "A":
                                pass
                            else:
                                card = valuedict[card[0]]

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

                        # Negate colour if card placed is Ace
                        if card[0] == "A":
                            if len(group) == index_position:
                                if (last_card_num == "13" or
                                        last_card_num == 13):
                                    return False
                                else:
                                    return True
                            elif index_position == 0:
                                if (first_card_num == "2" or
                                        first_card_num == 2):
                                    return False
                                else:
                                    return True
                            else:
                                return False

                        # Check whether card is of same colour and satisfies
                        # the run.
                        if (int(card) == int(last_card_num) + 1 and
                                cardcolour == colour):
                            if last_card_num == "13" or last_card_num == 13:
                                return False
                            if len(group) == index_position:
                                return True
                            else:
                                return False

                        elif (int(card) == int(first_card_num) - 1 and
                                cardcolour == colour):
                            if first_card_num == "2" or first_card_num == 2:
                                return False
                            if index_position == 0:
                                return True
                            else:
                                return False
                        else:
                            return False

    # Condition for discarding a card from the hand.
    elif play[0] == 5:
        # Invalid move if player has already discarded (or haven't drawn).
        if last_move == 5:
            return False
        # Invalid move if card is not in hand.
        if play[1] in hand:
            return True
        else:
            return False
