import random

def get_user_choice():
    choice = input("Enter rock, paper, scissors, or 'q' to quit: ").lower()
    while choice not in ['rock', 'paper', 'scissors', 'q']:
        choice = input("Invalid choice. Please enter rock, paper, scissors, or 'q' to quit: ").lower()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return 'tie'
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return 'win'
    else:
        return 'lose'

def play():
    user_score = 0
    computer_score = 0
    rounds_played = 0

    print("=== Rock, Paper, Scissors Game ===")
    print("Type 'rock', 'paper', or 'scissors' to play.")
    print("Type 'q' to quit the game.\n")

    while True:
        user_choice = get_user_choice()
        if user_choice == 'q':
            print("\nThanks for playing!")
            print(f"Final Score - You: {user_score}, Computer: {computer_score}, Rounds: {rounds_played}")
            break

        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        if result == 'win':
            print("You win this round!")
            user_score += 1
        elif result == 'lose':
            print("Computer wins this round!")
            computer_score += 1
        else:
            print("It's a tie!")

        rounds_played += 1
        print(f"Score => You: {user_score}, Computer: {computer_score}")
        print("-" * 30)

if __name__ == "__main__":
    play()
