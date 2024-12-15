from unittest import TestCase
from game_cards.Card import Card

class TestCard(TestCase):
    def setUp(self):
        self.card1 = Card(14,4) # Ace of clubs
        self.card2 = Card(9,4) # 9 of clubs
        self.card3 = Card(9,2) # 9 of Spade
        self.card4 = Card(2,1) # 2 of Diamond

# ------------------------------------------------ initialization tests ------------------------------------------------

    def test_invalid_card_value_type(self):
        with self.assertRaises(TypeError):
            card = Card('9',2) # Invalid card value type

    def test_invalid_card_suit_type(self):
        with self.assertRaises(TypeError):
            card = Card(9,'2') # Invalid card suit type

    def test_valid_low_limit_value(self):
        self.assertEqual(2,self.card4.value) # Valid lowest limit range value

    def test_valid_upper_limit_value(self):
        self.assertEqual(14,self.card1.value) # Valid upper limit range value

    def test_valid_value(self):
        self.assertEqual(9,self.card2.value) # Valid middle range value

    def test_invalid_low_limit_value_range(self):
        with self.assertRaises(ValueError):
            card = Card(1,2) # Invalid card value low limit

    def test_invalid_upper_limit_value_range(self):
        with self.assertRaises(ValueError):
            card = Card(15,2) # Invalid card value upper limit

    def test_valid_low_limit_suit(self):
        self.assertEqual(1, self.card4.suit)  # Valid lowest limit range suit

    def test_valid_upper_limit_suit(self):
        self.assertEqual(4,self.card1.suit) # Valid upper limit range suit

    def test_valid_suit(self):
        self.assertEqual(2,self.card3.suit) # Valid middle range suit

    def test_invalid_low_limit_suit_range(self):
        with self.assertRaises(ValueError):
            card = Card(9,0) # Invalid card suit low limit

    def test_invalid_upper_limit_suit_range(self):
        with self.assertRaises(ValueError):
            card = Card(9,5) # Invalid card suit upper limit

# ------------------------------------------------ gt func tests --------------------------------------------------

    def test_greater_value(self):
        # Test when one card has a higher value
        self.assertTrue(self.card1 > self.card2)

    def test_equal_value_higher_suit(self):
        # Test when values are equal, but one card has a higher suit
        self.assertTrue(self.card2 > self.card3)

    def test_less_than(self):
        # Test when the first card is less than the second
        self.assertFalse(self.card4 > self.card3)

    def test_equal_cards(self):
        # Test when both cards are the same
        card1 = Card(11, 2)  # Jack of Spades
        card2 = Card(11, 2)  # Jack of Spades
        self.assertFalse(card1 > card2)  # They are equal, so card1 is not greater than card2

    def test_invalid_gt_compare_type(self):
        # Test when comparing a card to not card object
        with self.assertRaises(TypeError):
            self.card1 > 42  # Comparing to an integer


# ------------------------------------------------ eq func tests --------------------------------------------------

    def test_invalid_eq_compare_type(self):
        # Test when comparing a card to not card object
        with self.assertRaises(TypeError):
            self.card1 == 42  # Comparing to an integer

    def test_valid_equal_cards(self):
        # Test when comparing a card to equal card
        card1 = Card(11, 2)  # Jack of Spades
        card2 = Card(11, 2)  # Jack of Spades
        self.assertTrue(card1 == card2)

    def test_valid_not_equal_cards_value(self):
        # Test when comparing not equal cards when only value different
        card1 = Card(9, 2)  # 9 of Spades
        card2 = Card(11, 2)  # Jack of Spades
        self.assertFalse(card1 == card2)

    def test_valid_not_equal_cards_suit(self):
        # Test when comparing not equal cards when only suit different
        card1 = Card(11, 3)  # Jack of Heart
        card2 = Card(11, 2)  # Jack of Spades
        self.assertFalse(card1 == card2)