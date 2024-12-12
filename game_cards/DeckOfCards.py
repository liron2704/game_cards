import random
from Card import Card

class DeckOfCards:
    def __init__(self):
        """
        Initialize the deck of cards.
        The deck is created by creating 52 diffrent cards of object Card
        with values(2-14) and suits(1-4)
        """
        self.cards = []
        for value in range(2, 15):  # Value range from 2 to 14 (Ace is 14)
            for suit in range(1, 5):  # Suit range from 1 to 4 (Diamond, Spade, Heart, Club)
                # Create a new card object and append it to the deck
                self.cards.append(Card(value, suit))

    def cards_shuffle(self):
        """
        Shuffle the deck of cards using random.shuffle.
        """
        random.shuffle(self.cards)

    def deal_one(self):
        """
        Deal one random card from the deck.
        It picks a random index, removes the card at that index from the deck, and returns it.
        """
        if len(self.cards) == 0:  # Check if the deck is empty
            raise ValueError("Cannot deal a card: the deck is empty.")

        random_index = random.randint(0, len(self.cards) - 1)  # Pick a random index from the deck
        removed_card = self.cards.pop(random_index)  # Remove and return the card
        return removed_card




