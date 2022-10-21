"""
5 Card Draw Poker
By Taylor Harrison a.k.a. HACKERMAN
"""
from random import shuffle

money: float = 1000

# the values of the cards as strings in a list
values = [
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "Jack",
    "Queen",
    "King",
    "Ace",
]
# the suites of the cards as strings in a list
suites = [
    "Hearts",
    "Clubs",
    "Diamonds",
    "Spades",
]

# the deck is a list of 2 strings- values and suites

flush: bool = False

# list of the cards that well  be dealt to the dealer, this isn't being used right now
dealer_cards = []

# function that deals 5 cards to the player.
def draw_5_cards():
    for i in range(5):
        # adding the 0th indexed card in deck[] to the players cards (your_cards)
        your_cards.append(deck[0])
        # remove the 0th indexed card in deck[] so that it's no longer in the deck, like in real life, duh
        deck.remove(deck[0])


# function to remove a number of cards (your_cards) specified by the player, then add new cards from the deck in their place
def remove_cards(cards_to_remove):
    # variable that takes the number passed from the player and turns that into a list of strings, one for each number
    x = list(cards_to_remove)
    # variable that evaluates each element in x and turns it into a list of integers
    y = [eval(i) for i in x]
    # variable that takes list y and subtracts 1 from each number since computers are stupid and start counting from 0
    q = [(i - 1) for i in y]
    # remove the ith indexed card from player's cards
    for i, v in enumerate(q):
        your_cards.pop(q[i])
        # insert the first card from the deck into player's cards, at the same index of the card that was removed
        your_cards.insert(q[i], deck[0])
        # remove the ith indexed card in deck[] so that it's no longer in the deck of cards
        deck.remove(deck[0])


# Function to check if there's a flush
def flush_check(cards):
    flush: bool = False
    my_suits: list = []
    # for each of the cards, create a list of the suits
    for i in range(5):
        my_suits.append(cards[i][1])
    # Create a set of the suits
    s = len(set(my_suits))
    # if the length of the set is 1, then all the suits are the same and you have a Flush!
    if s < 2:
        flush = True
        return flush
    else:
        return False


def four_kind(cards):
    my_nums: list = []
    for i in range(len(cards)):
        my_nums.append(cards[i][0])
    for i in range(len(my_nums)):
        item_count = my_nums.count(my_nums[i])
        if item_count == 4:
            return True
    return False


def three_kind(cards):
    my_nums: list = []
    for i in range(len(cards)):
        my_nums.append(cards[i][0])
    for i in range(len(my_nums)):
        item_count = my_nums.count(my_nums[i])
        if item_count == 3:
            return True
    return False


def two_pair(cards):
    two_pair: bool = False
    my_values: list = []
    # for each of the cards, create a list of the values
    for i in range(5):
        my_values.append(cards[i][0])
    s = len(set(my_values))  # Create a set of the values
    # if the length of the set is 1, then all the suits are the same and you have a Flush!
    if s == 3:
        two_pair = True
        return two_pair
    else:
        return False


def full_house(cards):
    full_house: bool = False
    my_values: list = []
    # for each of the cards, create a list of the values
    for i in range(5):
        my_values.append(cards[i][0])
    s = len(set(my_values))  # Create a set of the values
    # if the length of the set is 1, then all the suits are the same and you have a Flush!
    if s == 2:
        full_house = True
        return full_house
    else:
        return False


def pair(cards):
    my_nums: list = []
    for i, v in enumerate(cards):
        my_nums.append(cards[i][0])
    for j, q in enumerate(my_nums):
        item_count = my_nums.count(my_nums[j])
        if item_count == 2:
            return True
    return False


def straight(cards):
    my_nums_int = []
    my_nums: list = []
    for count, ele in enumerate(cards):
        my_nums.append(cards[count][0])
    for i, card in enumerate(my_nums):
        if card == "Jack":
            my_nums.pop(i)
            my_nums.insert(i, "11")
        if card == "Queen":
            my_nums.pop(i)
            my_nums.insert(i, "12")
        if card == "King":
            my_nums.pop(i)
            my_nums.insert(i, "13")
        if card == "Ace":
            my_nums.pop(i)
            my_nums.insert(0, "1")
            my_nums.insert(i - 1, "14")

    for i, ele in enumerate(my_nums):
        my_nums_int.append(eval(my_nums[i]))
    my_nums_int.sort()
    if len(my_nums_int) == 5:
        if (
            my_nums_int[0] == (my_nums_int[1] - 1)
            and my_nums_int[0] == (my_nums_int[2] - 2)
            and my_nums_int[0] == (my_nums_int[3] - 3)
            and my_nums_int[0] == (my_nums_int[4] - 4)
        ):
            return True
    if len(my_nums_int) == 6:
        if (
            my_nums_int[1] == (my_nums_int[2] - 1)
            and my_nums_int[1] == (my_nums_int[3] - 2)
            and my_nums_int[1] == (my_nums_int[4] - 3)
            and my_nums_int[1] == (my_nums_int[5] - 4)
        ):
            return True
        elif (
            my_nums_int[0] == (my_nums_int[1] - 1)
            and my_nums_int[0] == (my_nums_int[2] - 2)
            and my_nums_int[0] == (my_nums_int[3] - 3)
            and my_nums_int[0] == (my_nums_int[4] - 4)
        ):
            return True
        else:
            return False


print("5 Card Draw Poker 💲 💰 💵\n")

while money > 0:
    deck = [[v, s] for s in suites for v in values]
    # "shuffle" is a function that randomizes the order of the items in the list, deck
    shuffle(deck)
    # deck = deck[::-1] # reverse the order of the deck
    # list of the cards that will be dealt to the player
    your_cards = []
    try:
        bet: float = float(
            input(f"Enter the amount you want to bet, you have 💲{money:.2f}: ")
        )
        if bet > money:
            print(f"You don't have enough money, enter a lower amount")
        else:
            draw_5_cards()  # call function to draw 5 cards
            print(f"\n{your_cards}")  # print the cards to the user
            # prompt the user for which cards to remove, the values that will work are 1-5, press enter for no card removale
            cards_to_remove = input("\nWhich cards do you want to remove? ")
            # remove the cards and then add cards
            remove_cards(cards_to_remove)
            # print the new set of cards to the user (your_cards)
            print(f"\n{your_cards}")
            # Check if there's a flush, straight, pair etc...
            if flush_check(your_cards) and straight(your_cards):
                money = money + bet * 50
                print(f"\nYou have a straight flush! You won 💲{bet*50:.2f}!\n")
            elif flush_check(your_cards):
                money = money + bet * 5
                print(f"\nYou have a flush! You won 💲{bet*5:.2f}!\n")
            elif straight(your_cards):
                money = money + bet * 4
                print(f"\nYou have a straight! You won 💲{bet*4:.2f}!\n")
            elif four_kind(your_cards):
                money = money + bet * 30
                print(f"\nFour of a kind! You won 💲{bet*30:.2f}!\n")
            elif full_house(your_cards):
                money = money + bet * 7
                print(f"\nFull House! You won 💲{bet*7:.2f}!\n")
            elif three_kind(your_cards):
                money = money + bet * 3
                print(f"\nThree of a kind! You won 💲{bet*3:.2f}!\n")
            elif two_pair(your_cards):
                money = money + bet * 2
                print(f"\nTwo pair! You won 💲{bet*2:.2f}!\n")
            elif pair(your_cards):
                money = money + bet * 1.5
                print(f"\nYou have a pair! You won 💲{bet*1.5:.2f}!\n")
            else:
                money = money - float(bet)
                print(f"\nYou lost, you have 💲{money:.2f} remaining\n")
    except ValueError:
        print("You must enter a valid number")

print("You are out of 💰, game over! 💸💸💸")
