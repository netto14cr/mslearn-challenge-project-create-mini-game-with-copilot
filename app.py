import random

# Function to get the computer's choice
def get_computer_choice():
    options = ['rock', 'paper', 'scissors']
    return random.choice(options)

# Function to determine the winner
def determine_winner(player, computer):
    if player == computer:
        return "It's a tie"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper') or \
         (player == 'paper' and computer == 'rock'):
        return "Player wins"
    else:
        return "Computer wins"

# Main game function
def play_game():
    player_score = 0
    computer_score = 0
    rounds = 0

    while True:
        player = input("Choose rock, paper, or scissors: ").lower()

        if player not in ['rock', 'paper', 'scissors']:
            print("Invalid option. Please try again.")
            continue

        computer = get_computer_choice()
        print(f"The computer chooses: {computer}")

        result = determine_winner(player, computer)
        print(f"Round result: {result}")

        if result == "Player wins":
            player_score += 1
        elif result == "Computer wins":
            computer_score += 1

        rounds += 1

        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print(f"\nGame over. You played {rounds} rounds.")
    print(f"Player's victories: {player_score}")
    print(f"Computer's victories: {computer_score}")

if __name__ == "__main__":
    play_game()
