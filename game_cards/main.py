from CardGame import CardGame

if __name__ == "__main__":
    # Get player names
    player1_name = input("Enter the name of Player 1: ")
    player2_name = input("Enter the name of Player 2: ")

    # Start the game
    game = CardGame(player1_name, player2_name, 26)

    # Print initial hands
    print("\nInitial Hands:")
    print(game.player1)
    print(game.player2)

    # Run 10 rounds of the game
    print("\nStarting the game:")
    for round_num in range(1, 11):
        print(f"\nRound {round_num}:")

        # Each player plays a card
        card1 = game.player1.get_card()
        card2 = game.player2.get_card()

        print(f"{game.player1.player_name} played: {card1}")
        print(f"{game.player2.player_name} played: {card2}")

        # Print the winner of the round
        if card1 > card2:
            print(f"{game.player1.player_name} wins this round!")
            game.player1.add_card(card1)
            game.player1.add_card(card2)
        elif card2 > card1:
            print(f"{game.player2.player_name} wins this round!")
            game.player2.add_card(card1)
            game.player2.add_card(card2)
        else:
            print("It's a tie! No cards for anyone.") # Should never happen with 1 card deck

    # Print the final winner
    print("\nGame Over:")
    winner = game.get_winner()
    if winner is None:
        print("The game is a tie!")
    else:
        print(f"The winner is {winner.player_name}!")