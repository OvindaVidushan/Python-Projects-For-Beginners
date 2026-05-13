**How the Game Works**
```
1.The program randomly selects a word from a list of secret words.
2.The player has limited chances to guess the word.
3.When a correct letter is guessed, it is revealed in its correct position.
4.The player wins if all letters are guessed before running out of chances.
5.For simplicity, the program gives word length + 2 chances.
```
**Explanation:**
```
someWords.split(' '): Converts the string of words into a list.
word = random.choice(someWords): Selects a random secret word for the game.
chances = len(word) + 2: Sets number of chances based on word length.
guess = input(...).lower(): Takes a single letter input from the player.
if not guess.isalpha() ... Validates the input for letters only and uniqueness.
letterGuessed += guess * word.count(guess): Adds correctly guessed letters to the guessed list.
if chances <= 0 ... Ends the game if the player runs out of chances.
```
**Output**
```
Guess the word! HINT: word is a fruit.
_ _ _ _ _

Enter a letter to guess: m
m _ _ _ _ 
Enter a letter to guess: a
m a _ _ _ 
Enter a letter to guess: n
m a n _ _ 
Enter a letter to guess: g
m a n g _ 
Enter a letter to guess: o
m a n g o 
Congratulations! You guessed the word: mango
```
