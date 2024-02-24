import random

def get_user_choice():
    """
    Get the user's choice of Rock, Paper, or Scissors.
    """
    while True:
        user_choice = input("Enter your choice (Rock/Paper/Scissors): ").strip().capitalize()
        if user_choice in ['Rock', 'Paper', 'Scissors']:
            return user_choice
        else:
            print("Invalid choice. Please enter Rock, Paper, or Scissors.")

def get_computer_choice():
    """
    Generate a random choice for the computer: Rock, Paper, or Scissors.
    """
    return random.choice(['Rock', 'Paper', 'Scissors'])

def determine_winner(user_choice, computer_choice):
    """
    Determine the winner of the game based on the user's and computer's choices.
    """
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
        (user_choice == 'Paper' and computer_choice == 'Rock') or \
        (user_choice == 'Scissors' and computer_choice == 'Paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    """
    Main function to play the Rock, Paper, Scissors game.
    """
    print("Welcome to Rock, Paper, Scissors!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Entry point of the program
if __name__ == "__main__":
    play_game()
