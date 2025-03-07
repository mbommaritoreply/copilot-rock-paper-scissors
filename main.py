# Write a rock, paper, scissors, lizard, Spock game
# import random module
import random

def get_computer_choice(choices):
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and (computer_choice == "scissors" or computer_choice == "lizard")) or \
         (user_choice == "paper" and (computer_choice == "rock" or computer_choice == "spock")) or \
         (user_choice == "scissors" and (computer_choice == "paper" or computer_choice == "lizard")) or \
         (user_choice == "lizard" and (computer_choice == "spock" or computer_choice == "paper")) or \
         (user_choice == "spock" and (computer_choice == "scissors" or computer_choice == "rock")):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    choices = ["rock", "paper", "scissors", "lizard", "spock"]
    
    print("Choose your option:")
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice.capitalize()}")
    
    user_choice_index = int(input("Enter the number of your choice: ")) - 1
    user_choice = choices[user_choice_index]
    
    computer_choice = get_computer_choice(choices)
    
    print("Computer choice:", computer_choice)
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    main()
