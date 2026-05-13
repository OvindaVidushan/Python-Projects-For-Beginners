import random                     # Used to randomly pick a word from the list
from collections import Counter   # Helps compare guessed letters with the actual word

# List of fruit names as a single string
someWords = '''apple banana mango strawberry orang grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon'''

# Convert the long string into a list of words
someWords = someWords.split()

# Randomly choose one fruit from the list
word = random.choice(someWords)

if __name__ == '__main__':
    print('Guess the word! HINT: word is a fruit.')

    # Print underscores equal to the length of the chosen word
    for _ in word:
        print('_', end='')
    print()

    letterGuessed = ''            # Stores all correctly guessed letters
    chances = len(word) + 2       # Total chances given to the player
    flag = 0                      # Flag to check if the word is guessed

    try:
        # Game loop runs until chances run out or the word is guessed
        while chances > 0 and flag == 0:
            print()
            chances -= 1          # Reduce chances after each attempt

            try:
                guess = input('Enter a letter to Guess: ').lower()
            except:
                print('Enter only a letter!')
                continue

            # Input validation
            if not guess.isalpha():               # Only letters allowed
                print('Enter only a letter!')
                continue
            elif len(guess) > 1:                  # Only one letter allowed
                print('Enter only a single letter!')
                continue
            elif guess in letterGuessed:          # Avoid repeating guesses
                print('You already guessed that letter!')
                continue

            # If guessed letter is in the word
            if guess in word:
                # Add the letter as many times as it appears in the word
                letterGuessed += guess * word.count(guess)

            # Display the current progress of the word
            for char in word:
                if char in letterGuessed:
                    print(char, end='')
                else:
                    print('_', end='')

            # Check if all letters are guessed
            if Counter(letterGuessed) == Counter(word):
                print("\nCongratulations! You guessed the word:", word)
                flag = 1
                break

        # If chances are over and word not guessed
        if chances <= 0 and Counter(letterGuessed) != Counter(word):
            print("\nYou Lost! The word was:", word)

    except KeyboardInterrupt:
        print('\nGame Interrupted. Bye!')
        exit()
