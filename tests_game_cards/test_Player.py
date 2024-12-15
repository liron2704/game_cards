from unittest import TestCase
from game_cards.DeckOfCards import DeckOfCards
from game_cards.Card import Card
from game_cards.Player import Player
from unittest import mock


class TestPlayer(TestCase):
    def setUp(self):
        """Set up a Player and DeckOfCards instance for each test"""
        self.player = Player("TestPlayer", 15)
        self.deck = DeckOfCards()
        self.card = Card(4,2)

# ------------------------------------------------ Initialization Tests ------------------------------------------------

    def test_valid_name_initialization(self):
        """Test valid name of a Player"""
        self.assertEqual(self.player.player_name, "TestPlayer")

    def test_valid_num_of_cards_initialization(self):
        """Test valid number of cards of a Player"""
        self.assertEqual(self.player.num_of_cards_to_deal, 15)

    def test_valid_cards_list_empty_initialization(self):
        """Test player pack is empty"""
        self.assertEqual(len(self.player.cards), 0)

    def test_invalid_name_type(self):
        """Test invalid player name type"""
        with self.assertRaises(TypeError):
            Player(12, 15)

    def test_invalid_num_of_cards_type(self):
        """Test invalid number of cards type"""
        with self.assertRaises(TypeError):
            Player("TestPlayer", "15")

    def test_valid_num_of_cards_range_low_limit(self):
        """Test low limit of valid number of cards"""
        player = Player("TestPlayer", 10)
        self.assertEqual(player.num_of_cards_to_deal, 10)

    def test_valid_num_of_cards_range_high_limit(self):
        """Test high limit of valid number of cards"""
        player = Player("TestPlayer", 26)
        self.assertEqual(player.num_of_cards_to_deal, 26)

    def test_invalid_num_of_cards_range_low(self):
        """Test invalid number of cards below range"""
        with self.assertRaises(ValueError):
            Player("TestPlayer", 9)

    def test_invalid_num_of_cards_range_high(self):
        """Test invalid number of cards above range"""
        with self.assertRaises(ValueError):
            Player("TestPlayer", 27)

    def test_invalid_num_of_cards_changes_to_26(self):
        """Test invalid number of cards changes to 26"""
        with self.assertRaises(ValueError):
            player = Player("TestPlayer", 9)
            self.assertEqual(player.num_of_cards_to_deal,26)

# ------------------------------------------------- Set Hand Tests -----------------------------------------------------

    def test_set_hand_success(self):
        """Test set hand with valid deck"""
        self.player.set_hand(self.deck)
        self.assertEqual(len(self.player.cards), 15)

    def test_set_hand_success_low_limit(self):
        """Test set hand with valid deck low limit"""
        player = Player('TestPlayer',10)
        player.set_hand(self.deck)
        self.assertEqual(len(player.cards), 10)

    def test_set_hand_success_high_limit(self):
        """Test set hand with valid deck high limit"""
        player = Player('TestPlayer',26)
        player.set_hand(self.deck)
        self.assertEqual(len(player.cards), 26)

    def test_Invalid_set_hand_high_limit(self):
        """Test set hand with Invalid deck high limit"""
        with self.assertRaises(ValueError):
            player = Player('TestPlayer',27)
            player.set_hand(self.deck)
            self.assertEqual(len(player.cards), 26)

    def test_Invalid_set_hand_low_limit(self):
        """Test set hand with Invalid deck low limit"""
        with self.assertRaises(ValueError):
            player = Player('TestPlayer',9)
            player.set_hand(self.deck)
            self.assertEqual(len(player.cards), 26)

    def test_set_hand_removes_from_deck(self):
        """Test set hand removes the card from deck"""
        self.player.set_hand(self.deck)
        self.assertEqual(len(self.deck.cards), 37)

    def test_set_hand_removes_from_deck_low_limit(self):
        """Test set hand removes the card from deck low limit"""
        player = Player('TestPlayer', 10)
        player.set_hand(self.deck)
        self.assertEqual(len(self.deck.cards), 42)

    def test_set_hand_removes_from_deck_high_limit(self):
        """Test set hand removes the card from deck high limit"""
        player = Player('TestPlayer', 26)
        player.set_hand(self.deck)
        self.assertEqual(len(self.deck.cards), 26)

    def test_set_hand_removes_from_deck_Invalid_cards_to_deal_high_limit(self):
        """Test set hand removes the card from deck with Invalid cards to deal number high limit"""
        with self.assertRaises(ValueError):
            player = Player('TestPlayer', 27)
            player.set_hand(self.deck)
            self.assertEqual(len(self.deck.cards), 26)

    def test_set_hand_removes_from_deck_Invalid_cards_to_deal_low_limit(self):
        """Test set hand removes the card from deck with Invalid cards to deal number low limit"""
        with self.assertRaises(ValueError):
            player = Player('TestPlayer', 9)
            player.set_hand(self.deck)
            self.assertEqual(len(self.deck.cards), 26)

    def test_set_hand_invalid_deck_type(self):
        """Test set hand with an invalid deck type"""
        with self.assertRaises(TypeError):
            self.player.set_hand("15")

    def test_set_hand_not_enough_cards(self):
        """Test set hand when the deck doesnt have enough cards"""
        player = Player("TestPlayer", 26)
        self.deck.cards = []
        with self.assertRaises(ValueError):
            self.player.set_hand(self.deck)

    def test_uniq_cards_deck(self):
        """Test that all cards in player deck are unique"""
        self.player.set_hand(self.deck)
        unique_dealt_cards = set(str(card) for card in self.player.cards)
        self.assertEqual(len(self.player.cards), len(unique_dealt_cards))

    @mock.patch('game_cards.DeckOfCards.DeckOfCards.deal_one', return_value=Card(12,2))
    def test_set_hand_deal_card(self,mock_obj):
        """Test that player deck have the card number of times he asked for"""
        self.player.set_hand(self.deck)
        cards_list = []
        for _ in range(15):
            cards_list.append(Card(12,2))
        self.assertEqual(cards_list,self.player.cards)



# ------------------------------------------------- Get Card Tests -----------------------------------------------------

    def test_type_return_value(self):
        """Test that return value of get card is type of Card"""
        player = Player("TestPlayer", 26)
        player.set_hand(DeckOfCards())
        card = player.get_card()
        self.assertIsInstance(card, Card)

    def test_enough_cards_in_deck_cards(self):
        """Test that get card reduce the number of the deck by 1"""
        player = Player("TestPlayer", 26)
        player.set_hand(DeckOfCards())
        player.get_card()
        self.assertEqual(len(player.cards), 25)

    def test_get_card_not_enough_cards(self):
        """Test get card when the player deck doesnt have enough cards"""
        player = Player("TestPlayer", 26)
        deck = DeckOfCards()
        player.set_hand(deck)
        for _ in range(player.num_of_cards_to_deal):
            player.get_card()
        with self.assertRaises(ValueError):
            self.player.get_card()

    def test_get_card_not_in_player_deck_after(self):
        """Test that removed card not in the players deck after get card"""
        player = Player("TestPlayer", 26)
        deck = DeckOfCards()
        player.set_hand(deck)
        removed_card = player.get_card()
        self.assertNotIn(removed_card,player.cards)


# ------------------------------------------------- Add Card Tests -----------------------------------------------------

    def test_add_card_type_error(self):
        """Test add card with invalid type"""
        with self.assertRaises(TypeError):
            self.player.add_card(5)
    
    def test_add_card_successfully(self):
        """Test that card added successfully to the player deck"""
        self.player.add_card(self.card)
        self.assertIn(self.card,self.player.cards)

    def test_add_card_deck_size_increase(self):
        """Test that player deck size increased by one"""
        self.player.add_card(self.card)
        self.assertEqual(len(self.player.cards),1)

    def test_add_card_successfully_with_cards_in_deck(self):
        """Test that card added successfully to the player deck with cards in deck"""
        self.player.set_hand(self.deck)
        self.player.add_card(self.card)
        self.assertIn(self.card, self.player.cards)

    def test_add_card_deck_size_increase_with_cards(self):
        """Test that player deck size increased by one when deck was with cards"""
        self.player.set_hand(self.deck)
        self.player.add_card(self.card)
        self.assertEqual(len(self.player.cards),16)




