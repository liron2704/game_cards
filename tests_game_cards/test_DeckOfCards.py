from unittest import TestCase
from game_cards.DeckOfCards import DeckOfCards
from game_cards.Card import Card


class TestDeckOfCards(TestCase):
    def setUp(self):
        """Create a new deck for each test"""
        self.deck = DeckOfCards()

    # ------------------------------------------------ initialization tests ------------------------------------------
    def test_full_deck(self):
        """Test that the deck initializes with 52 cards"""
        self.assertEqual(len(self.deck.cards), 52)

    def test_valid_cards_deck(self):
        # Generate a valid deck of cards as a set of string representations
        valid_deck = set(str(Card(value, suit)) for value in range(2, 15) for suit in range(1, 5))
        # Convert the cards in the deck to a set of string representations
        original_deck = set(str(card) for card in self.deck.cards)
        # Compare the two sets
        self.assertEqual(original_deck, valid_deck)

    def test_card_list_type(self):
        """Test that cards is a list"""
        self.assertIsInstance(self.deck.cards, list)

    # ------------------------------------------------ shuffle tests ------------------------------------------------
    def test_shuffle_changes_order(self):
        """Test that shuffling the deck changes the order of the cards"""
        original_order = list(self.deck.cards)  # Copy the original order
        self.deck.cards_shuffle()
        shuffled_order = list(self.deck.cards)
        self.assertNotEqual(original_order, shuffled_order)

    def test_same_len_cards_after_shuffle(self):
        """Length of deck dont change after shuffle"""
        original_order = list(self.deck.cards)  # Copy the original order
        self.deck.cards_shuffle()
        self.assertEqual(len(original_order), len(self.deck.cards))

    def test_deck_after_shuffle(self):
        """Test that the deck has the same cards after shuffling"""
        original_cards = set(str(card) for card in self.deck.cards)
        self.deck.cards_shuffle()
        shuffled_cards = set(str(card) for card in self.deck.cards)
        self.assertEqual(original_cards, shuffled_cards)

    # ------------------------------------------------ deal_one tests ------------------------------------------------

    def test_deal_one_size_reduce(self):
        """Test that deal_one reduce deck size by 1"""
        original_size = len(self.deck.cards)
        self.deck.deal_one()
        self.assertEqual(len(self.deck.cards), original_size - 1)

    def test_deal_one_return_card(self):
        """Test that deal_one returns the card"""
        dealt_card = self.deck.deal_one()
        self.assertIsInstance(dealt_card, Card)

    def test_deal_one_card_removed_from_deck(self):
        """Test that deal_one removes the card from the deck"""
        dealt_card = self.deck.deal_one()
        self.assertNotIn(dealt_card, self.deck.cards)

    def test_deal_one_until_empty(self):
        """Test that dealing all cards works correctly and raises an error when empty"""
        for _ in range(len(self.deck.cards)): # Range of 52 (pack size)
            self.deck.deal_one()
        self.assertEqual(len(self.deck.cards), 0) # Card deck is empty

    def test_deal_one_when_empty(self):
        """Test that raise error when deal card from empty deck"""
        for _ in range(len(self.deck.cards)): # Range of 52 (pack size)
            self.deck.deal_one()
        self.assertEqual(self.deck.deal_one(),None)

    def test_no_duplicate_cards_deal(self): # maybe unnecessary because we test no duplicates cards
        """Test that no dealing duplicate card"""
        dealt_cards = [self.deck.deal_one() for _ in range(52)]
        unique_dealt_cards = set(str(card) for card in dealt_cards)
        self.assertEqual(len(dealt_cards), len(unique_dealt_cards))
