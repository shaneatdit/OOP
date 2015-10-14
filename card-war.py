"""
Simulates the classic card game "War".

Creates a deck of cards, shuffles them, and deals them to two players.  Then plays the game.
"""

from random import shuffle

# SUITS = ["Hearts", "Diamonds", "Spades", "Clubs"]
SUITS = ["Hearts"]      # Need an small, odd number of cards to avoid stalemate
FACES = {2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six",
         7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Jack",
         12: "Queen", 13: "King", 14: "Ace"}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        self.face = FACES[self.rank]
        description = "The " + self.face + " of " + self.suit
        return description


def create_and_shuffle_deck():
    # Create deck of cards
    deck = []
    for suit in SUITS:
        for rank in FACES:
            deck.append(Card(suit, rank))
    shuffle(deck)
    return deck


def deal_cards(deck):
    """Divides cards into two lists and returns the two lists"""
    player1_pile = []
    player2_pile = []
    for j in range(len(deck)):
        card = deck.pop(0)
        if j % 2 == 0:
            player1_pile.append(card)
        else:
            player2_pile.append(card)
    return player1_pile, player2_pile


def main():
    # Create and shuffle deck
    deck = create_and_shuffle_deck()

    # Deal cards
    player1_pile, player2_pile = deal_cards(deck)

    # Play the game
    battle = 0
    while len(player1_pile) > 0 and len(player2_pile) > 0:
        battle += 1
        print()
        print("Battle ", battle, ":", sep="")
        card1 = player1_pile.pop(0)
        card2 = player2_pile.pop(0)
        print("Player 1:", card1, ":: Player 2:", card2)

        if card1.rank > card2.rank:
            player1_pile.append(card1)
            player1_pile.append(card2)
            print("Player 1 wins.")
            print("Score:", len(player1_pile), ":", len(player2_pile))
        elif card2.rank > card1.rank:
            player2_pile.append(card1)
            player2_pile.append(card2)
            print("Player 2 wins.")
            print("Score:", len(player1_pile), ":", len(player2_pile))
        else:
            player1_pile.append(card1)
            player2_pile.append(card2)
            print("Draw.")
            print("Score:", len(player1_pile), ":", len(player2_pile))

    # Print result
    print()
    if len(player2_pile) == 0:
        print("WINNER: PLAYER 1!")
    elif len(player1_pile) == 0:
        print("WINNER: PLAYER 2!")

main()
