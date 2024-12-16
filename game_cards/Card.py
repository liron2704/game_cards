class Card:
    def __init__(self, value, suit):
        """
        Initialize the Card class.
        value: The value of the card (Ace, King, Queen, Jack...). (integer)
        suit: The suit of the card (Diamond, Spade, Heart, Club). (integer)
        """
        if not isinstance(value, int):
            raise TypeError("value must be an integer.")
        if not isinstance(suit, int):
            raise TypeError("Suit must be an integer.")
        if value < 2 or value > 14:
            raise ValueError("value must be between 2 to 14")
        if suit < 1 or suit > 4:
            raise ValueError("suit must be between 1 to 4")

        self.value = value
        self.suit = suit

    def __repr__(self):
        """Return the string representation of the card."""
        value_values = {
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "10",
            11: "Jack",
            12: "Queen",
            13: "King",
            14: "Ace"  # Ace is the highest value
        }
        suit_values = {
            1: "Diamond",
            2: "Spade",
            3: "Heart",
            4: "Club"
        }
        return f"{value_values[self.value]} of {suit_values[self.suit]}"



    def __gt__(self, other):
        """
        Compare two cards by their values.
        If the values are equal, compare by suit value.
        """
        if not isinstance(other, Card):
            raise TypeError("Can only compare Card instances.")

        if self.value == other.value and self.suit == other.suit:
            return False

        if self.value != other.value:
            return self.value > other.value
        return self.suit > other.suit  # Compare suits if values are equal

    def __eq__(self, other):
        """Check if 2 cards are equal"""
        if not isinstance(other, Card):
            raise TypeError("Can only compare Card instances.")
        return self.value == other.value and self.suit == other.suit


