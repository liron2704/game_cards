from game_cards.DeckOfCards import DeckOfCards
from game_cards.Card import Card
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
            num_of_cards_to_deal = 26  # Default to 26 if out of range

        self.player_name = player_name
        self.num_of_cards_to_deal = num_of_cards_to_deal
        self.cards = []  # Initialize an empty list to hold the players cards

    def __str__(self):
        return f"Player: {self.player_name}, Cards: {self.cards}"

    def set_hand(self, deck_of_cards: DeckOfCards):
        """Set the players hand by dealing a specified number of cards from the deck."""
        if not isinstance(deck_of_cards, DeckOfCards):
            raise TypeError("Deck of cards must be DeckOfCards type.")
        if len(deck_of_cards.cards) < self.num_of_cards_to_deal: # Not enough cards to deal
            self.num_of_cards_to_deal = len(deck_of_cards.cards)
        for _ in range(self.num_of_cards_to_deal):
            self.cards.append(deck_of_cards.deal_one())  # Add cards to the players cards list

    def get_card(self):
        """Get random card from players cards list."""
        if len(self.cards) <= 0:
            return
        random_index = random.randint(0, len(self.cards) - 1)  # Pick a random index
        return self.cards.pop(random_index)  # Remove and return the card

    def add_card(self, card: Card):
        """Add a card to players cards list"""
        if not isinstance(card, Card):
            raise TypeError("You can only add a Card object to the players hand.")
        self.cards.append(card)  # Add the card to the players cards list
