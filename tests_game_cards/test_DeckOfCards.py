from unittest import TestCase
from game_cards.DeckOfCards import DeckOfCards
from game_cards.Card import Card


class TestDeckOfCards(TestCase):
    def setUp(self):
        """Create a new DeckOfCards instance for each test"""
        self.deck = DeckOfCards()

    # ------------------------------------------------ initialization tests ------------------------------------------
    def test_full_deck(self):
        """Test that the deck initializes with 52 unique cards"""
        self.assertEqual(len(self.deck.cards), 52)

    def test_unique_cards(self):
        """Check that all cards are unique"""
        unique_cards = set(str(card) for card in self.deck.cards)
        print(unique_cards)
        self.assertEqual(len(unique_cards), 52)

    def test_card_values(self):
        """Test that all card values in range."""
        for card in self.deck.cards:
            self.assertIn(card.value, range(2, 15), "Card value should be between 2 and 14")

    def test_card_suits(self):
        """Card suits should be between 1 and 4."""
        for card in self.deck.cards:
            self.assertIn(card.suit, range(1, 5), "Card suit should be between 1 and 4")

    # ------------------------------------------------ shuffle tests ------------------------------------------------
    def test_shuffle_changes_order(self):
        """Test that shuffling the deck changes the order of the cards"""
        original_order = list(self.deck.cards)  # Copy the original order
        self.deck.cards_shuffle()
        shuffled_order = list(self.deck.cards)
        self.assertNotEqual(original_order, shuffled_order)

    def test_same_len_cards_after_shuffle(self):
        """Length of deck do no change after shuffle"""
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
        self.assertEqual(len(self.deck.cards), original_size - 1)

    def test_deal_one_return_card(self):
        """"Test that deal_one returns the card"""
        dealt_card = self.deck.deal_one()
        self.assertIsInstance(dealt_card, Card)

    def test_deal_one_card_removed_from_deck(self):
        """Test that deal_one removes the card from the deck"""
        dealt_card = self.deck.deal_one()
        self.assertNotIn(dealt_card, self.deck.cards)

    def test_deal_one_until_empty(self):
        """Test that dealing all cards works correctly and raises an error when empty"""
        for _ in range(52):
            self.deck.deal_one()
        self.assertEqual(len(self.deck.cards), 0)

    def test_deal_one_when_empty(self):
        """Test that raise error when deal card from empty deck"""
        for _ in range(52):
            self.deck.deal_one()
        with self.assertRaises(ValueError):
            self.deck.deal_one()

    def test_no_duplicate_cards_deal(self):
        """Test that no dealing duplicate card"""
        dealt_cards = [self.deck.deal_one() for _ in range(52)]
        unique_dealt_cards = set(str(card) for card in dealt_cards)
        self.assertEqual(len(dealt_cards), len(unique_dealt_cards))

# def test_invalid_test_set_hand_lowest_cards(self):

#     try:

#         player = Player("Avi", 9)

#         #self.assertEqual(player.number_of_cards, 26)

#         self.assertEqual(len(player.cards) , 26)

#     except Exception as e:

#         print(f"{e}")


# def test_invalid_set_hand_lowest_cards(self):
#     with self.assertRaises(ValueError):
#         player = Player("Avi", 9)
#
#         player.set_hand(DeckOfCards())
#
#         self.assertEqual(player.number_of_cards, 26)
#
#
# def test_invalid_set_hand_highest_cards(self):
#     with self.assertRaises(ValueError):
#         player = Player("Avi", 27)
#
#         player.set_hand(DeckOfCards())
#
#         self.assertEqual(player.number_of_cards, 26)