import random
#Guess the number (Computer)
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x} : '))
        if guess < random_number:
            print("Sorry guess again. It's too low")
        if guess > random_number:
            print("Sorry guess again. It's too high")
    
    print(f"Congratulations!. You've guessed the number correctly {random_number}")
guess(10)
