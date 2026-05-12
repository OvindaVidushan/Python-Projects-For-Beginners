import random  #importing the random module

name= input("What is Your Name?") #getting the user name, and greeting the user
print("Good Luck!",name)

#list of words and choosing a random word
words=["raindow","computer","science","programming","python","mathematics","player","condition","reverse","water","board","geeks"]

word=random.choice(words) #selecets a random word from the words list

print("Guess the characters") #promting useer to guess

guesses=""  #initializing guessed and turns
turns=12

while turns > 0:     #checking each character in the word
    failed = 0
    for char in word:
            if char in guesses:
                print(char, end="")
            else:
                print("_")
                failed+=1
    if failed == 0:                     #checking if user has won
        print("You Win")
        print("The word is:",word)
        break
    print()
    guess = input("guess the character:") #promting for the next guess
    
    guesses += guess

    if guess not in word:               #handling the incorrect guesses
        turns -= 1
        print("Wrong")
        print("You Have",+turns,"more guesses")
    
    if turns == 0:                       #checking if the user has lost
        print("You Loose")
                