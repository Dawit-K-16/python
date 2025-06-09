import random

num = random.randint(1, 100)
guess = None

while guess != num:
    guess = int(input("Enter your guess: "))
    
    if guess > num:
        print("Too high")
    elif guess < num:
        print("Too low")
    else:
        print("Correct! You guessed it!")
