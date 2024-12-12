from DeckOfCards import DeckOfCards
from Player import Player

class CardGame:
    def __init__(self, player1_name, player2_name, num_of_cards_to_deal):
        """
        Initialize the CardGame.
        player1_name (str): The name of the first player.
        player2_name (str): The name of the second player.
        num_of_cards_to_deal (int): The number of cards to deal to each player.
        """
        if not isinstance(player1_name, str) or not isinstance(player2_name, str):
            raise TypeError("Player names must be strings.")
        if not isinstance(num_of_cards_to_deal, int):
            raise TypeError("Number of cards to deal must be an integer.")

        # Create the deck and players
        self.deck_of_cards = DeckOfCards()
        self.player1 = Player(player1_name, num_of_cards_to_deal)
        self.player2 = Player(player2_name, num_of_cards_to_deal)

        # Set a flag to track initialization
        self._is_initializing = True

        # Start the game
        self.new_game()

        # Clear the initialization flag
        self._is_initializing = False

    def new_game(self):
        """
        Start a new game by shuffling the deck and dealing cards to the players.
        """
        if not self._is_initializing:
            raise RuntimeError("new_game can only be called during initialization (__init__).")

        # Shuffle the deck and deal cards to both players
        self.deck_of_cards.cards_shuffle()
        self.player1.set_hand(self.deck_of_cards)
        self.player2.set_hand(self.deck_of_cards)

    def get_winner(self):
        """
        return the winner based on the number of who have more cards
        None: If both players have the same number of cards.
        """
        if len(self.player1.cards) == len(self.player2.cards):
            return None  #tie
        if len(self.player1.cards) > len(self.player2.cards):
            return self.player1  # Player 1 has more cards
        return self.player2  # Player 2 has more cards