import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors:\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'Tie'
    if iswin(user, computer):
        return 'You won!'
    
    return 'You lost!'

def iswin(player, opponent):
    # return True if player beats opponent
    if (player == 'r' and opponent == 's') or \
       (player == 's' and opponent == 'p') or \
       (player == 'p' and opponent == 'r'):
        return True
    return False

# Run the game
print(play())
