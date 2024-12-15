from unittest import TestCase
from game_cards.DeckOfCards import DeckOfCards
from game_cards.Card import Card
from game_cards.Player import Player


class TestPlayer(TestCase):
    def setUp(self):
        """Set up a Player and DeckOfCards instance for each test"""
        self.player = Player("TestPlayer", 15)
        self.deck = DeckOfCards()

    def test_valid_name_initialization(self):
        """Test valid initialization of a Player"""
        self.assertEqual(self.player.player_name, "TestPlayer")

    def test_valid_num_of_cards_initialization(self):
        """Test valid initialization of a Player"""
        self.assertEqual(self.player.num_of_cards_to_deal, 15)

    def test_valid_cards_list_empty_initialization(self):
        """Test valid initialization of a Player"""
        self.assertEqual(len(self.player.cards), 0)

    def test_invalid_name_type(self):
        """Test invalid player name type"""
        with self.assertRaises(TypeError):
            Player(12345, 15)

    def test_invalid_num_of_cards_type(self):
        """Test invalid number of cards type"""
        with self.assertRaises(TypeError):
            Player("TestPlayer", "15")

    def test_invalid_num_of_cards_range_low(self):
        """Test invalid number of cards below range"""
        with self.assertRaises(ValueError):
            Player("TestPlayer", 9)

    def test_invalid_num_of_cards_range_high(self):
        """Test invalid number of cards above range"""
        with self.assertRaises(ValueError):
            Player("TestPlayer", 27)