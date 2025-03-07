import pytest
from main import get_computer_choice, determine_winner

def test_get_computer_choice():
    choices = ["rock", "paper", "scissors", "lizard", "spock"]
    computer_choice = get_computer_choice(choices)
    assert computer_choice in choices

@pytest.mark.parametrize("user_choice, computer_choice, expected", [
    ("rock", "scissors", "You win!"),
    ("rock", "lizard", "You win!"),
    ("paper", "rock", "You win!"),
    ("paper", "spock", "You win!"),
    ("scissors", "paper", "You win!"),
    ("scissors", "lizard", "You win!"),
    ("lizard", "spock", "You win!"),
    ("lizard", "paper", "You win!"),
    ("spock", "scissors", "You win!"),
    ("spock", "rock", "You win!"),
    ("rock", "rock", "It's a tie!"),
    ("paper", "paper", "It's a tie!"),
    ("scissors", "scissors", "It's a tie!"),
    ("lizard", "lizard", "It's a tie!"),
    ("spock", "spock", "It's a tie!"),
    ("rock", "paper", "Computer wins!"),
    ("rock", "spock", "Computer wins!"),
    ("paper", "scissors", "Computer wins!"),
    ("paper", "lizard", "Computer wins!"),
    ("scissors", "rock", "Computer wins!"),
    ("scissors", "spock", "Computer wins!"),
    ("lizard", "rock", "Computer wins!"),
    ("lizard", "scissors", "Computer wins!"),
    ("spock", "paper", "Computer wins!"),
    ("spock", "lizard", "Computer wins!"),
])
def test_determine_winner(user_choice, computer_choice, expected):
    assert determine_winner(user_choice, computer_choice) == expected