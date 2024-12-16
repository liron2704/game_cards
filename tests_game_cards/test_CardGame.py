from unittest import TestCase
from game_cards.CardGame import CardGame
from game_cards.DeckOfCards import DeckOfCards
from game_cards.Player import Player
from game_cards.Card import Card
from unittest import mock


class TestCardGame(TestCase):
    def setUp(self):
        self.card_game = CardGame('TestPlayer1','TestPlayer2',26)
        self.player = Player('TestPlayer3',15)

# ------------------------------------------------ Initialization Tests ------------------------------------------------
    def test_invalid_player1_type_initialization(self):
        """Test invalid player1 name type"""
        with self.assertRaises(TypeError):
            CardGame(5,'TestPlayer2',15)

    def test_invalid_player2_type_initialization(self):
        """Test invalid player2 name type"""
        with self.assertRaises(TypeError):
            CardGame('TestPlayer1',[2,4,5],15)

    def test_invalid_num_of_cards_to_deal_type_initialization(self):
        """Test invalid cards to deal type"""
        with self.assertRaises(TypeError):
            CardGame('TestPlayer1','TestPlayer2', {15:'test'})

    def test_initialization_player1_name_successfully(self):
        """Test that valid player1 name initialization successfully"""
        self.assertEqual(self.card_game.player1.player_name,"TestPlayer1")

    def test_initialization_player2_name_successfully(self):
        """Test that valid player2 name initialization successfully"""
        self.assertEqual(self.card_game.player2.player_name,"TestPlayer2")

    def test_initialization_player1_number_of_cards_to_deal_successfully(self):
        """Test that valid player1 number of cards to deal initialization successfully"""
        self.assertEqual(self.card_game.player1.num_of_cards_to_deal,26)

    def test_initialization_player2_number_of_cards_to_deal_successfully(self):
        """Test that valid player2 number of cards to deal initialization successfully"""
        self.assertEqual(self.card_game.player2.num_of_cards_to_deal,26)

    def test_initialization_player2_number_of_cards_to_deal_successfully_low_limit(self):
        """Test that valid player2 number of cards to deal initialization successfully low limit"""
        card_game = CardGame('TestPlayer1','TestPlayer2',10)
        self.assertEqual(card_game.player2.num_of_cards_to_deal,10)

    def test_initialization_player2_number_of_cards_to_deal_successfully_high_limit(self):
        """Test that valid player2 number of cards to deal initialization successfully high limit"""
        card_game = CardGame('TestPlayer1','TestPlayer2',26)
        self.assertEqual(card_game.player2.num_of_cards_to_deal,26)

    def test_initialization_player1_number_of_cards_to_deal_successfully_low_limit(self):
        """Test that valid player1 number of cards to deal initialization successfully low limit"""
        card_game = CardGame('TestPlayer1','TestPlayer2',10)
        self.assertEqual(card_game.player1.num_of_cards_to_deal,10)

    def test_initialization_player1_number_of_cards_to_deal_successfully_high_limit(self):
        """Test that valid player1 number of cards to deal initialization successfully low limit"""
        card_game = CardGame('TestPlayer1','TestPlayer2',26)
        self.assertEqual(card_game.player1.num_of_cards_to_deal,26)

    def test_out_range_initialization_player1_number_of_cards_to_deal_low_limit(self):
        """
        Test that invalid player1 number of cards to deal initialization successfully low limit
        Initialize number of cards to deal to 26
        """
        card_game = CardGame('TestPlayer1','TestPlayer2',9)
        self.assertEqual(card_game.player1.num_of_cards_to_deal,26)

    def test_out_range_initialization_player1_number_of_cards_to_deal_high_limit(self):
        """
        Test that invalid player1 number of cards to deal initialization successfully high limit
        Initialize number of cards to deal to 26
        """
        card_game = CardGame('TestPlayer1','TestPlayer2',27)
        self.assertEqual(card_game.player1.num_of_cards_to_deal,26)

    def test_out_range_initialization_player2_number_of_cards_to_deal_low_limit(self):
        """
        Test that invalid player2 number of cards to deal initialization successfully low limit
        Initialize number of cards to deal to 26
        """
        card_game = CardGame('TestPlayer1','TestPlayer2',9)
        self.assertEqual(card_game.player2.num_of_cards_to_deal,26)

    def test_out_range_initialization_player2_number_of_cards_to_deal_high_limit(self):
        """
        Test that invalid player2 number of cards to deal initialization successfully high limit
        Initialize number of cards to deal to 26
        """
        card_game = CardGame('TestPlayer1','TestPlayer2',27)
        self.assertEqual(card_game.player2.num_of_cards_to_deal,26)

    def test_is_initialization_False(self):
        """Test that initialization flag is False after initialization"""
        self.assertFalse(self.card_game.is_initializing)

    def test_deck_cards_is_created(self):
        """Test that deck card has been created with 52 cards"""
        deck = DeckOfCards()
        self.card_game.deck_of_cards = DeckOfCards()
        self.assertEqual(len(deck.cards), len(self.card_game.deck_of_cards.cards))

    def test_unique_deck_of_cards(self):
        """Test that the deck in CardGame contains unique cards"""
        cards_in_deck = self.card_game.deck_of_cards.cards
        unique_cards = set((card.value, card.suit) for card in cards_in_deck)
        # Assert that the number of unique cards equals the total cards in the deck
        self.assertEqual(len(cards_in_deck), len(unique_cards))

    @mock.patch('game_cards.CardGame.CardGame.new_game')
    def test_new_game_called_once(self,mock_new_game):
        """Test that new_game was called exactly once during initialization"""
        CardGame("Player1", "Player2", 26)
        mock_new_game.assert_called_once()



# ------------------------------------------------ New Game Tests --------------------------------------------------

    def test_new_game_not_in_initialization(self):
        """Test invalid func new_game call not from initialization"""
        with self.assertRaises(RuntimeError):
            self.card_game.new_game()

# ------------------------------------------------ Get Winner Tests --------------------------------------------------

    def test_get_winner_tie(self):
        """Test that get winner returns None if its tie"""
        card1 = Card(5,2)
        card2 = Card(7,3)
        card3 = Card(12,3)
        card4 = Card(11,4)
        self.card_game.player1.cards = [card1,card2]
        self.card_game.player2.cards = [card3,card4]
        self.assertIsNone(self.card_game.get_winner())

    def test_get_winner_player1_win(self):
        """Test new game returns player1 wins when he wins"""
        card1 = Card(5,2)
        card2 = Card(7,3)
        card3 = Card(12,3)

        self.card_game.player1.cards = [card1,card2]
        self.card_game.player2.cards = [card3]
        self.assertEqual(self.card_game.player1,self.card_game.get_winner())

    def test_get_winner_player2_win(self):
        """Test new game returns player2 wins when he wins"""
        card1 = Card(5,2)
        card2 = Card(7,3)
        card3 = Card(12,3)

        self.card_game.player1.cards = [card1]
        self.card_game.player2.cards = [card3,card2]
        self.assertEqual(self.card_game.player2,self.card_game.get_winner())


