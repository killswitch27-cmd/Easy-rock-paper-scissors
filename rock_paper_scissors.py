import random


# Computer makes a random choice between rock, paper and scissors
def computer_choice():
    move = ['r', 'p', 's']
    return random.choice(move)

    
# Logic to determine winner of the game
def determine_winner(player, computer):
    if player == computer:
        return "It's a tie"
    
    # rock beats scissor, scissor beats paper, paper beats rock
    winner = {
        "r" : "s",
        "s" : "p",
        "p" : "r"
    }
    
    if winner[player] == computer:
        return "Player WINS!"
    else:
        return "Computer WINS!"
    
    
# Reads player choice and compares it with the computer choice to determine winner
def play_game():
    valid_choices = {'r', 'p', 's'}
    
    while True:
        player = input("\nEnter your move: ").strip()
        
        if player in valid_choices:
            break
        print("Invalid Choice")
    
    computer = computer_choice()
     
    decisions = {
        "r" : "Rock",
        "p" : "Paper",
        "s" : "Scissor"
    }
    
    print("You chose", decisions[player])
    print("Computer chose", decisions[computer])
    
    print(determine_winner(player, computer))

while True:
    play_game()
    
    