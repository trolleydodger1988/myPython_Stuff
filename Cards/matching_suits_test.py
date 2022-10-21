pair: bool = False
three_kind: bool = False
four_kind: bool = False

# wildcard_pattern = "_"
your_cards = [
    ["King", "Spaids"],
    ["King", "Hearts"],
    ["King", "Diamonds"],
    ["Jack", "Hearts"],
    ["Queen", "Spaids"],
]

print(your_cards)
my_nums: list = []
"""
# print(your_cards.count(your_cards[0]))
for i in range(5):
    my_nums.append(your_cards[i][0])

print(my_nums)

for i in range(4):
    item_count = my_nums.count(my_nums[i])
    if item_count == 3:
        three_kind = True

print(three_kind)
"""


def equal_suits(cards):
    my_suits: list = []
    for i in range(5):
        my_suits.append(cards[i][1])
    s = len(set(my_suits))
    if s < 2:
        print("Flush")


def two_three_four_kind(cards):
    pair: bool = False
    three_kind: bool = False
    four_kind: bool = False
    my_nums: list = []
    for i in range(len(cards)):
        my_nums.append(cards[i][0])
    print(my_nums)
    for i in range(len(my_nums)):
        item_count = my_nums.count(my_nums[i])
        # print(f"{three_kind}{four_kind}")
        print(item_count)
        if item_count == 4:
            four_kind = True
        elif item_count == 3:
            three_kind = True
            print("three of a kind")

        elif item_count == 2:
            pair = True
        else:
            one = 1
    # return four_kind, three_kind, pair


equal_suits(your_cards)
two_three_four_kind(your_cards)
print(three_kind)
if three_kind == True:
    print("Three of a kind")
