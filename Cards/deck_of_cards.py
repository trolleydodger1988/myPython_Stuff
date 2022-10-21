from random import shuffle

values = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']     # the values of the cards as strings in a list
suites = ['Hearts', 'Clubs', 'Diamonds', 'Spades']                              # the suites of the cards as strings in a list
deck = [[v, s] for s in suites for v in values]                                 #the deck is a list of 2 strings- values and suites

shuffle(deck)       # "shuffle" is a function that randomizes the order of the items in the list, deck
your_cards = []     # list of the cards that will be dealt to the player
dealer_cards = []   # list of the cards that well  be dealt to the dealer, this isn't being used right now

def draw_5_cards():                 # function that deals 5 cards to the player. 
    for i in range(0,5):
        your_cards.append(deck[i])  # adding the ith indexed card in deck[] to the players cards (your_cards)
        deck.remove(deck[i])        # remove the ith indexed card in deck[] so that it's no longer in the deck, like in real life, duh

def remove_cards(cards_to_remove):  # function to remove a number of cards (your_cards) specified by the player, then add new cards from the deck in their place
    x = list(cards_to_remove)       # variable that takes the number passed from the player and turns that into a list of strings, one for each number
    y = [eval(i) for i in x]        # variable that evaluates each element in x and turns it into a list of integers 
    q = [(i-1) for i in y]          # variable that takes list y and subtracts 1 from each number since computers are stupid and start counting from 0 
    for i, v in enumerate(q):         
        your_cards.pop(q[i])                # remove the ith indexed card from player's cards
        your_cards.insert(q[i],deck[0])     # insert the first card from the deck into player's cards, at the same index of the card that was removed
        deck.remove(deck[i])                # remove the ith indexed card in deck[] so that it's no longer in the deck of cards

draw_5_cards()                                                  # call function to draw 5 cards
print(your_cards)                                               # print the cards to the user
cards_to_remove = input("Which cards do you want to remove? ")  # prompt the user for which cards to remove, the values that will work are 1-5, press enter for no card removale
remove_cards(cards_to_remove)                                   # remove the cards and then add cards
print(your_cards)                                               # print the new set of cards to the user (you_cards)

