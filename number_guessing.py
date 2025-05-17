import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    guess_counter = 0

    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        guess_counter += 1

        if guess < random_number:
            print("Guess higher")
        elif guess > random_number:
            print("Guess lower")

    print(f"Nice guess! You guessed it in {guess_counter} tries!")    
        
guess(10)


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low!= high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)'.lower())
        if feedback =='h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'the computer guess your number {guess} correctly!')
computer_guess(10)