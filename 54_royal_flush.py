import euler_functions

lines = euler_functions.open_txt('https://projecteuler.net/resources/documents/0054_poker.txt')

card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13,
               'A': 14}
hand_rankings = {"High Card": 1, "One Pair": 2, "Two Pair": 3, "Three of a Kind": 4, "Straight": 5, "Flush": 6,
                 "Full House": 7, "Four of a Kind": 8, "Straight Flush": 9, "Royal Flush": 10}


def card_value(card):
    return card_values[card[0]]

def evaluate_hand(hand):
    values = [card[0] for card in hand]
    suits = [card[1] for card in hand]

    def is_straight(numbers):
        if len(set(numbers)) != 5:
            return False
        value_numbers = sorted([card_values[number] for number in set(numbers)])
        return value_numbers == list(range(min(value_numbers), max(value_numbers) + 1))

    value_counts = {value: values.count(value) for value in set(values)}
    sorted_values = sorted(value_counts.items(), key=lambda x: (-x[1], x[0]))

    num_unique_values = len(value_counts)

    suit_counts = {suit: suits.count(suit) for suit in set(suits)}
    num_unique_suits = len(suit_counts)

    if num_unique_suits == 1:
        if set(values) == {'A', 'K', 'Q', 'J', 'T'}:
            return "Royal Flush"
        elif is_straight(values):
            return "Straight Flush", hand[0][0]
    if num_unique_values == 2:
        if 4 in value_counts.values():
            return "Four of a Kind", sorted_values[0], [card[0] for card in hand]
        if sorted_values[0][1] == 3 and sorted_values[1][1] == 2:
            return "Full House", sorted_values[0], sorted_values[1]

    if num_unique_suits == 1:
        return "Flush", [card[0] for card in hand]

    if is_straight(values):
        return "Straight", [card[0] for card in hand]



    if num_unique_values == 3:
        if sorted_values[0][1] == 3:
            return "Three of a Kind", sorted_values[0][0], [card[0] for card in hand]
        if sorted_values[0][1] == 2:
            pair1_value = sorted_values[0]
            pair2_value = sorted_values[1]
            return "Two Pair", max(pair1_value, pair2_value), min(pair1_value, pair2_value), [card[0] for card in hand]



    if 2 in value_counts.values():
        return "One Pair", sorted_values[0][0], [card[0] for card in hand], sorted_values

    return "High Card", [card[0] for card in hand]


def compare_hands(hand1, hand2):
    hand1_eval = evaluate_hand(hand1)
    hand2_eval = evaluate_hand(hand2)
    if hand_rankings[hand1_eval[0]] > hand_rankings[hand2_eval[0]]:
        return hand1
    if hand_rankings[hand1_eval[0]] < hand_rankings[hand2_eval[0]]:
        return "Loss or tie don't care"
    else:
        k = 1
        while k < len(hand1_eval):
            if isinstance(hand1_eval[k], str):
                if card_values[hand1_eval[k]] > card_values[hand2_eval[k]]:
                    return hand1
                if card_values[hand1_eval[k]] < card_values[hand2_eval[k]]:
                    return "Loss or tie don't care"
                k += 1
            else:
                for i in range(len(hand1_eval[k])):
                    if card_values[hand1_eval[k][i]] > card_values[hand2_eval[k][i]]:
                        return hand1
                    if card_values[hand1_eval[k][i]] < card_values[hand2_eval[k][i]]:
                        return "Loss or tie don't care"

player_1_wins = 0

for line in lines:
    hands = [line[i:i + 14].strip() for i in range(0, len(line), 15)]
    hand1 = sorted(hands[0].split(), key=card_value, reverse=True)
    hand2 = sorted(hands[1].split(), key=card_value, reverse=True)
    if compare_hands(hand1, hand2) == hand1:
        player_1_wins += 1
        #print("Win", evaluate_hand(hand1), evaluate_hand(hand2))
print(player_1_wins)