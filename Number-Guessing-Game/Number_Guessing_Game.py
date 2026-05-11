import random   # Imports Python's random module so we can generate random numbers

# Printing a welcome message for the player
print("-----------------------------------------------------\n"
"Hi, Welcome to the Number Guessing Game!\n"
"You have 7 chances to guess the Number. Let's Start!!!\n"
"-----------------------------------------------------")

# Asking the user to enter the lower and upper bounds for the random number
low  = int(input("Enter the Lower Bound = "))
high = int(input("Enter the Upper Bound = "))

# Informing the user about the number of chances and the range
print(f"\n*** You have 7 chances to guess the number between {low} and {high}. Let's Start!!! ***\n")

# Generating a random number between the given lower and upper bounds
num = random.randint(low, high)

ch = 7   # Total allowed chances
gc = 0   # Guess counter (how many guesses the user has used)

# Loop runs until the user uses all chances
while gc < ch:
    gc += 1   # Increase guess count by 1 each time
    guess = int(input("Enter your guess = "))

    # If the guess is correct
    if guess == num:
        print(f"Correct! The number is {num}. You guessed it in {gc} chances.")
        break   # Exit the loop because the game is won

    # If this is the last chance and the guess is still wrong
    elif gc >= ch and guess != num:
        print(f"Sorry! The number was {num}. Better luck next time.")

    # If the guess is higher than the actual number
    elif guess > num:
        print("Too high! Try a lower number.")

    # If the guess is lower than the actual number
    elif guess < num:
        print("Too low! Try a higher number.")
import random   # Imports Python's random module so we can generate random numbers

# Printing a welcome message for the player
print("-----------------------------------------------------\n"
"Hi, Welcome to the Number Guessing Game!\n"
"You have 7 chances to guess the Number. Let's Start!!!\n"
"-----------------------------------------------------")

# Asking the user to enter the lower and upper bounds for the random number
low  = int(input("Enter the Lower Bound = "))
high = int(input("Enter the Upper Bound = "))

# Informing the user about the number of chances and the range
print(f"\n*** You have 7 chances to guess the number between {low} and {high}. Let's Start!!! ***\n")

# Generating a random number between the given lower and upper bounds
num = random.randint(low, high)

ch = 7   # Total allowed chances
gc = 0   # Guess counter (how many guesses the user has used)

# Loop runs until the user uses all chances
while gc < ch:
    gc += 1   # Increase guess count by 1 each time
    guess = int(input("Enter your guess = "))

    # If the guess is correct
    if guess == num:
        print(f"Correct! The number is {num}. You guessed it in {gc} chances.")
        break   # Exit the loop because the game is won

    # If this is the last chance and the guess is still wrong
    elif gc >= ch and guess != num:
        print(f"Sorry! The number was {num}. Better luck next time.")

    # If the guess is higher than the actual number
    elif guess > num:
        print("Too high! Try a lower number.")

    # If the guess is lower than the actual number
    elif guess < num:
        print("Too low! Try a higher number.")
