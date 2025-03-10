import pytest
from main import determine_winner, get_computer_choice

@pytest.mark.parametrize("user_choice, computer_choice, expected", [
    ("rock", "rock", "It's a tie!"),
    ("rock", "scissors", "You win!"),
    ("rock", "lizard", "You win!"),
    ("rock", "paper", "Computer wins!"),
    ("rock", "spock", "Computer wins!"),
    ("paper", "rock", "You win!"),
    ("paper", "spock", "You win!"),
    ("paper", "scissors", "Computer wins!"),
    ("paper", "lizard", "Computer wins!"),
    ("paper", "paper", "It's a tie!"),
    ("scissors", "paper", "You win!"),
    ("scissors", "lizard", "You win!"),
    ("scissors", "rock", "Computer wins!"),
    ("scissors", "spock", "Computer wins!"),
    ("scissors", "scissors", "It's a tie!"),
    ("lizard", "spock", "You win!"),
    ("lizard", "paper", "You win!"),
    ("lizard", "rock", "Computer wins!"),
    ("lizard", "scissors", "Computer wins!"),
    ("lizard", "lizard", "It's a tie!"),
    ("spock", "scissors", "You win!"),
    ("spock", "rock", "You win!"),
    ("spock", "paper", "Computer wins!"),
    ("spock", "lizard", "Computer wins!"),
    ("spock", "spock", "It's a tie!")
])
def test_determine_winner(user_choice, computer_choice, expected):
    assert determine_winner(user_choice, computer_choice) == expected

def test_get_computer_choice():
    assert get_computer_choice() in ["rock", "paper", "scissors", "lizard", "spock"]