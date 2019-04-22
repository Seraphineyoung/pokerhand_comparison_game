import random

values = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J":11, "Q":12, "K":13, "A":14}
suits = ["S", "C", "H", "D"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
royalFlush = ['KS', 'TS', 'JS', 'QS', 'AS']
flush = ['AC', 'JD', '2C', 'QC', 'TC'] 
straight = ['AS', 'JS', 'KS', 'QS', 'TS']
straightF = ['3S', '6S', '5S', '7S', '4S']
four_of_a_kind = ['3S', '3C', '3D', '3H', '5S']
full_house = ['3S', '3C', '3D', '2H', '2S']

deck = []
for suit in suits:
    for rank in ranks:
        deck.append((f"{rank}{suit}"))
# print(deck)

def hand_to_array(string_hand):
    hand = string_hand.upper().split(" ")
    #checking if the player hand is found amoung the deck and the length is equal to 5
    assert set(hand).issubset(deck) and len(hand) == 5
    return sort_hand(hand)

def sort_hand(hand):
    #sort hand with the first element of each card, based on values
    hand_sorted = sorted(hand, key=lambda s:values[s[0]])
    return hand_sorted

def count_frequency(hand):
    #gettin all the ranks in hand
    ranks = [rank[0] for rank in hand]
    #counting the frquency in ranks
    rank_frequency = {rank : ranks.count(rank) for rank in ranks}
    return rank_frequency

def check_is_flush(player):
    suits = [suit[1] for suit in player]
    return len(set(suits)) == 1

# print(check_is_flush(flush),"flush")

def check_is_straight(player):
    ranks = [rank[0] for rank in player]
    string_rank = ''.join(ranks)
    is_consecutive = string_rank in '23456789TJQKA'
    return is_consecutive
       
# print(check_is_straight(straight))

def check_is_four_of_a_kind(player):
    player_frequency = count_frequency(player)
    if 4 in player_frequency.values():
        return True
    return False

def check_is_fullhouse(player):
    player_frequency = count_frequency(player)
    if (3 in player_frequency.values()) and (2 in player_frequency.values()) :
        return True
    return False

def compare_hands(hand1,hand2,hand_value):
    if hand1 and not hand2:
        return (f"hand1 = 1,{hand_value}") 
    if hand2 and not hand1:
       return(f"hand2 = 1,{hand_value}") 
    if hand1 and hand2:
        return (f"hand1 and hand 2 = {3},{hand_value}")
    if not hand1 and not hand2:
        return False

# check if straightflush and ten2ace
def check_royal_flush(player):
    suits = [suit[1] for suit in player]
    ranks = [rank[0] for rank in player]
    royal_flush_ranks = ['A', 'Q', 'T', 'J', 'K']
    ten_to_ace = (set(ranks) == set(royal_flush_ranks))
    if ten_to_ace and len(set(suits)) == 1:
        return True
    return False

def isRoyal_flush():
    hand_value = "Royal flush"
    player_1 = input("Enter hand: ")
    sort_hand_a = hand_to_array(player_1)
    player_2 = input("Enter hand: ")
    sort_hand_b = hand_to_array(player_2)
    hand1 = check_royal_flush(sort_hand_a)
    hand2 = check_royal_flush(sort_hand_b)
    is_royal_flush = compare_hands(hand1, hand2, hand_value)
    if is_royal_flush:
        return print(is_royal_flush)
    return is_straight_flush(sort_hand_a,sort_hand_b)


def is_straight_flush(hand_a,hand_b):
    hand_value = "straight flush"
    hand1 = check_is_flush(hand_a) and check_is_straight(hand_a)
    hand2 = check_is_flush(hand_b) and check_is_straight(hand_b)
    straight_flush = compare_hands(hand1,hand2,hand_value)
    if straight_flush:
        return print(straight_flush)
    return is_four_of_a_kind(hand_a,hand_b)


def is_four_of_a_kind(hand_a,hand_b):
    hand_value = "Four of a kind"
    hand1 = check_is_four_of_a_kind(hand_a)
    hand2 = check_is_four_of_a_kind(hand_b)
    four_of_a_kind = compare_hands(hand1,hand2,hand_value)
    if four_of_a_kind:
        return print(four_of_a_kind)
    return is_full_house(hand_a,hand_b)


def is_full_house(hand_a,hand_b):
    hand_value = "Full House"
    hand1 = check_is_fullhouse(hand_a)
    hand2 = check_is_fullhouse(hand_b)
    full_house = compare_hands(hand1,hand2,hand_value)
    if full_house:
        return print(full_house)
    return is_flush(hand_a,hand_b)
 
def is_flush(hand_a,hand_b):
    hand_value = "Flush"
    hand1 = check_is_flush(hand_a)
    hand2 = check_is_flush(hand_b)
    is_a_flush = compare_hands(hand1,hand2,hand_value)
    if is_a_flush:
        return print(is_a_flush)
    return is_straight(hand_a,hand_b)


def is_straight(hand_a,hand_b):
    hand_value = "Straight"
    hand1 = check_is_straight(hand_a)
    hand2 = check_is_straight(hand_b)
    is_a_straight = compare_hands(hand1,hand2,hand_value)
    if is_a_straight:
        return print(is_a_straight)
    return three_of_a_kind(hand_a,hand_b)
    

isRoyal_flush()




