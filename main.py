import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors", "lizard", "spock"])

def determine_winner(user_choice, computer_choice):
    winning_combinations = {
        "rock": ["scissors", "lizard"],
        "paper": ["rock", "spock"],
        "scissors": ["paper", "lizard"],
        "lizard": ["spock", "paper"],
        "spock": ["scissors", "rock"]
    }
    if user_choice == computer_choice:
        return "It's a tie!"
    elif computer_choice in winning_combinations[user_choice]:
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
    computer_choice = get_computer_choice()
    
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(determine_winner(user_choice, computer_choice))

if __name__ == "__main__":
    main()