"""
Creates a class that represents a single playing card.

Then creates a deck of 52 cards, shuffles them, and then prints the shuffled deck.

Chooses a random card from the deck and prints it.
"""
from random import shuffle, randint

SUITS = ["Hearts", "Diamonds", "Spades", "Clubs"]
FACES = {2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Jack",
         12: "Queen", 13: "King", 14: "Ace"}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        self.face = FACES[self.rank]
        description = "The " + self.face + " of " + self.suit
        return description


def main():
    # Create deck of cards
    deck = []
    for suit in SUITS:
        for rank in FACES:
            deck.append(Card(suit, rank))

    # Print deck
    print()
    print("Unshuffled deck:")
    for i in range(len(deck)):
        print(deck[i])
        # Insert a blank line after each suit
        if i % 13 == 12:
            print()

    # Shuffle deck
    shuffle(deck)

    # Print shuffled deck
    print("Shuffled deck:")
    for card in deck:
        print(card)

    # Selects a random card from the deck
    n = randint(0, len(deck) - 1)
    random_card = deck[n]
    print()
    print("Today's card is:", random_card)

main()
