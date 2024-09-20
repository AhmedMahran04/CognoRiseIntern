import random

def computer():
    computer_choices = ["rock","paper","scissors"]
    return random.choice(computer_choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "scissors" and computer_choice == "paper") or \
            (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "Computer wins :("

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\n    Rock, Paper, Scissors Game    ")
        print("Type 'rock', 'paper', or 'scissors' to play.")

        user_choice = input("Enter your choice: ").lower()

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice, please choose 'rock', 'paper', or 'scissors'.")
            continue

        computer_choice = computer()

        winner = determine_winner(user_choice, computer_choice)

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win!")
            user_score += 1
        else:
            print("You lose :(")
            computer_score += 1

        print(f"\nScores: You: {user_score}, Computer: {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Final Scores:")
            print(f"You: {user_score}, Computer: {computer_score}")
            break


play_game()
