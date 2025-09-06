import random

# Check functions

def toggleCheck():
    while True:
        try:
            toggle = input("Would you like to play? (y/n): ").lower()
            if toggle == 'y' or toggle == 'n':
                return toggle
                break
            else:
                print("Please enter either (y) or (n)!")
        except ValueError:
            print("Invalid input.")

def tryCheck():
    while True:
        try:
            tries = int(input("How many tries would you like? (Must be at least 1): "))
            if tries >= 1:
                return tries
                break
            else:
                print("Please enter a number of tries greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def hintCheck():
    while True:
        try:
            hints = input("Would you like hints? (y/n): ").lower()
            if hints == 'y' or hints == 'n':
                return hints
                break
            else:
                print("Please enter either (y) or (n)")
        except ValueError:
            print("Invalid input.")



def guessCheck(gameOver, toggle, number, maxNum):
    while True:
        try:
            guess = int(input(f"What's your guess? You have {tries} {"try" if tries == 1 else "tries"}: "))
            if guess > -1 and guess < maxNum:
                return guess
                break

           
            else:
                print(f"Please enter a valid number between 1 and {maxNum} (or type 0 to give up).")
        except ValueError:
                print(f"Invalid input. Please enter a number between 1 and {maxNum} (or type 0 to give up).")


def maxCheck():
    while True:
        try:
            maxNum = int(input("What's the maximum value the number can be (min = 1)? "))
            if maxNum > 1:
                return maxNum
                break
            else:
                print("Please enter a value greater than 1.")
        except ValueError:
            print("Invalid input. Please enter a number greater than 1.")


print("Welcome to 'Guess a Number!'")
toggle = toggleCheck()

while toggle == 'y':
    gameOver = False

    maxNum = maxCheck()
    number = random.randint(1, maxNum)
    tries = tryCheck()
    hints = hintCheck()
    guess = guessCheck(gameOver, toggle, number, maxNum)




    while not gameOver:

        if guess == number:
            print(f"Correct! The number was {number}")
            gameOver = True
            toggle = 'n'
        
        # Feedback when the guess is more than max or less than 1
        if guess == 0:
            print(f"The number was {number}")
            gameOver = True
            toggle = 'n'

        # Feedback when the guess is wrong
        elif guess != number:
            tries -= 1
            guess = int(input(f"Try again! You have {tries} {"try" if tries == 1 else "tries"} left (to give up, type 0): "))
            if hints == 'y':
                if guess > number:
                    print("Your number is too high!")
                elif guess < number:
                    print("Your number is too low!")

        if tries == 1:            
            print("You're out of tries!")
            print(f"The number was {number}!")
            gameOver = True
            toggle = 'n'