import random

# Map numbers to moves
MOVES = {0: "Rock", 1: "Paper", 2: "Scissors"}

def get_computer_move():
    """Generate a random move for the computer."""
    return random.randint(0, 2)

def get_user_move():
    """Get the user's move with input validation."""
    print("\nChoose your move:")
    for key, value in MOVES.items():
        print(f"{key}: {value}")
    while True:
        try:
            move = int(input("Enter your move (0, 1, or 2): "))
            if move in MOVES:
                return move
            else:
                print("Invalid input. Please choose 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def determine_winner(player_a, player_b):
    """
    Determine the winner based on the moves.
    Returns:
        -1 for tie, 0 if Player A wins, 1 if Player B wins.
    """
    if player_a == player_b:
        return -1
    elif (player_a == 0 and player_b == 2) or \
         (player_a == 1 and player_b == 0) or \
         (player_a == 2 and player_b == 1):
        return 0
    else:
        return 1

def display_result(player_a, player_b, winner):
    """Display the game result."""
    print(f"\nPlayer A chose: {MOVES[player_a]}")
    print(f"Player B chose: {MOVES[player_b]}")

    if winner == -1:
        print("It's a Tie!")
    elif winner == 0:
        print("Player A Wins!")
    else:
        print("Player B Wins!")

def play_round():
    """Simulate a single round of the game."""
    print("\n--- Rock, Paper, Scissors ---")
    print("Choose Game Mode:")
    print("1. User vs Computer")
    print("2. Computer vs Computer")
    while True:
        try:
            mode = int(input("Enter game mode (1 or 2): "))
            if mode in [1, 2]:
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    if mode == 1:
        player_a = get_user_move()
    else:
        player_a = get_computer_move()

    player_b = get_computer_move()
    winner = determine_winner(player_a, player_b)
    display_result(player_a, player_b, winner)
    return winner

def game_statistics(stats):
    """Display game statistics."""
    total_rounds = sum(stats.values())
    print("\n--- Game Statistics ---")
    print(f"Total Rounds Played: {total_rounds}")
    print(f"Player A Wins: {stats['player_a_wins']}")
    print(f"Player B Wins: {stats['player_b_wins']}")
    print(f"Ties: {stats['ties']}")

def main():
    """Main game loop."""
    stats = {"player_a_wins": 0, "player_b_wins": 0, "ties": 0}

    print("Welcome to the Enhanced Rock, Paper, Scissors Game!")
    while True:
        winner = play_round()
        if winner == -1:
            stats["ties"] += 1
        elif winner == 0:
            stats["player_a_wins"] += 1
        else:
            stats["player_b_wins"] += 1

        again = input("\nDo you want to play another round? (y/n): ").strip().lower()
        if again != 'y':
            break

    game_statistics(stats)
    print("\nThanks for playing! Goodbye!")

if __name__ == "__main__":
    main()
