"""
Bryan Dingman
Find the chances of winning if you 'hit' when you are at 17 or not in a game of 21
"""

# Needed for array shuffle
import random

# Set up our variables
iterations = 100000
deck = []
defeat = 0
win = 0
likely = 0

# Create our deck. Face cards are considered 10s
for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    if num != 10:
        for i in range(0, 4):
            deck.append(num)
    else:
        for i in range(0, 16):
            deck.append(num)

# Our master loop
for num in range(0, iterations):

    # Set our current hand to 17
    currentHand = 17

    # Shuffle our deck
    random.shuffle(deck)

    # Select a card and add it to our hand
    currentHand += deck[len(deck) - 1]

    # Calculate if we busted, won, or didn't bust
    if currentHand < 21:
        likely += 1
    elif currentHand == 21:
        win += 1
    else:
        defeat += 1

# Print out the results
print "Defeats: {:.1f}%\n".format((float(defeat) / iterations) * 100), \
    "Certain Victories: {:.1f}%\n".format((float(win) / iterations) * 100), \
    "Likely Victories: {:.1f}%".format((float(likely) / iterations) * 100)
