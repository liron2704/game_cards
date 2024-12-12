from DeckOfCards import DeckOfCards
from Card import Card
import random


class Player:
    def __init__(self, player_name, num_of_cards_to_deal=26):
        """
        Initialize a Player object.
        player_name (str): The name of the player.
        num_of_cards_to_deal (int): Number of cards to deal to the player. Defaults to 26.
        """
        if not isinstance(player_name, str):
            raise TypeError("name must be a string.")
        if not isinstance(num_of_cards_to_deal, int):
            raise TypeError("number of cards to deal must be an integer.")
        if num_of_cards_to_deal < 10 or num_of_cards_to_deal > 26:
            self.num_of_cards_to_deal = 26  # Default to 26 if out of range
            raise ValueError(
                "number of cards to deal must be between 10 to 26 "
                "(initialized the number to default: 26)"
            )

        self.player_name = player_name
        self.num_of_cards_to_deal = num_of_cards_to_deal
        self.cards = []  # Initialize an empty list to hold the players cards

    def set_hand(self, deck_of_cards: DeckOfCards):
        """
        Set the players hand by dealing a specified number of cards from the deck.
        """
        if len(deck_of_cards.cards) < self.num_of_cards_to_deal:
            raise ValueError(
                f"Not enough cards in the deck to deal {self.num_of_cards_to_deal} cards."
            )
        for _ in range(self.num_of_cards_to_deal):
            self.cards.append(deck_of_cards.deal_one())  # Add cards to the players cards list

    def get_card(self):
        """
        Get random card from players cards list.
        """
        if len(self.cards) == 0:
            raise ValueError("Cannot get a card: the players hand is empty.")
        random_index = random.randint(0, len(self.cards) - 1)  # Pick a random index
        return self.cards.pop(random_index)  # Remove and return the card

    def add_card(self, card: Card):
        """
        Add a card to players cards list.
        """
        if not isinstance(card, Card):
            raise TypeError("You can only add a Card object to the players hand.")
        self.cards.append(card)  # Add the card to the players cards list
