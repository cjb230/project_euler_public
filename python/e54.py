import datetime

SOURCE_FILE = 'p054_poker.txt'
STRAIGHT_FLUSH = 1
FOUR_OF_A_KIND = 2
FULL_HOUSE = 3
FLUSH = 4
STRAIGHT = 5
THREE_OF_A_KIND = 6
TWO_PAIRS = 7
ONE_PAIR = 8
HIGH_CARD = 9


def rank_val(rank):
    if rank == 'A':
        return 14
    elif rank == 'K':
        return 13
    elif rank == 'Q':
        return 12
    elif rank == 'J':
        return 11
    elif rank == 'T':
        return 10
    else:
        return int(rank)


def is_flush(hand):
    if hand[0][1] == hand[1][1] and hand[0][1] == hand[2][1] and hand[0][1] == hand[3][1] and hand[0][1] == hand[4][1]:
        return True
    else:
        return False


def sorted_ranks(hand):
    ranks = dict()
    for card in hand:
        if rank_val(card[0]) in ranks:
            ranks[rank_val(card[0])] += 1
        else:
            ranks[rank_val(card[0])] = 1
    return ranks


def is_straight(ranks):
    if len(ranks) != 5:
        return False
    if min(ranks) + 4 == max(ranks):
        return True
    else:
        return False


def is_four_of_a_kind(ranks):
    if len(ranks) != 2:
        return False
    for rank, cnt in ranks.items():
        if cnt == 1 or cnt == 4:
            return True
        else:
            return False


def is_full_house(ranks):
    if len(ranks) != 2:
        return False
    for rank, cnt in ranks.items():
        if cnt == 2 or cnt == 3:
            return True
        else:
            return False


def is_three_of_a_kind(ranks):
    if len(ranks) != 3:
        return False
    for rank, cnt in ranks.items():
        if cnt == 3:
            return True
    return False


def is_two_pair(ranks):
    if len(ranks) != 3:
        return False
    one_found = False
    two_found = False
    for rank, cnt in ranks.items():
        if cnt == 1:
            one_found = True
        elif cnt == 2:
            two_found = True
    if one_found and two_found:
        return True
    else:
        return False


def is_pair(ranks):
    if len(ranks) == 4:
        return True
    else:
        return False


def rank_tie_breaker(ranks_hand_1, ranks_hand_2):
    if len(ranks_hand_1) != len(ranks_hand_2):
        print('RANKS ERROR')
        print(ranks_hand_1)
        print(ranks_hand_2)
        return -1
    resolved = False
    ranks_hand_1.sort()
    ranks_hand_2.sort()



def high_card_tie_breaker(hand_1, hand_2):
    rank_list_1 = list(sorted_ranks(hand_1))
    rank_list_2 = list(sorted_ranks(hand_2))
    resolved = False
    while not resolved:
        highest_card_1 = max(rank_list_1)
        highest_card_2 = max(rank_list_2)
        if highest_card_1 > highest_card_2:
            return 1
        elif highest_card_1 < highest_card_2:
            return 2
        else:






def hand_value(hand):
    hand_ranks = sorted_ranks(hand)
    flush = is_flush(hand)
    straight = is_straight(hand_ranks)

    if straight and flush:
       # print('SF:', hand)
        return STRAIGHT_FLUSH
    elif is_four_of_a_kind(hand_ranks):
      #  print('FK:', hand)
        return FOUR_OF_A_KIND
    elif is_full_house(hand_ranks):
     #   print('FH:', hand)
        return FULL_HOUSE
    elif flush:
    #    print('FL:', hand)
        return FLUSH
    elif straight:
   #     print('ST:', hand)
        return STRAIGHT
    elif is_three_of_a_kind(hand_ranks):
  #      print('TK:', hand)
        return THREE_OF_A_KIND
    elif is_two_pair(hand_ranks):
 #       print('2P:', hand)
        return TWO_PAIRS
    elif is_pair(hand_ranks):
#        print('PR:', hand)
        return ONE_PAIR
    else:
        return HIGH_CARD





def main():
    player_1_wins = 0
    player_2_wins = 0
    draws = 0

    with open(SOURCE_FILE) as f:
        file = f.readlines()
    for line in file:
        cards = line.replace('\n', '').split(' ')
        hand_1 = [cards[0], cards[1], cards[2], cards[3], cards[4]]
        hand_2 = [cards[5], cards[6], cards[7], cards[8], cards[9]]
        score_1 = hand_value(hand_1)
        score_2 = hand_value(hand_2)
        if score_1 < score_2:
            #print('player 1 wins:')
            player_1_wins += 1
            #print(score_1, hand_1)
            #print(score_2, hand_2)
            #print()
        elif score_2 < score_1:
            #print('player 2 wins:')
            player_2_wins += 1
            #print(score_2, hand_2)
            #print(score_1, hand_1)
            #print()
        else:
            if score_1 == 9:
                print('draw - ', score_1)
            draws += 1
            #print(score_1, hand_1)
            #print(score_2, hand_2)
            #print()

    print(player_1_wins)
    print(player_2_wins)
    print(draws)


if __name__ == "__main__":
    start = datetime.datetime.now()
    main()
    end = datetime.datetime.now()
    duration = end - start
    print(str(duration.total_seconds()) + " seconds")
