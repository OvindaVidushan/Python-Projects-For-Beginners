import random  #importing the random module

name= input("What is Your Name?") #getting the user name, and greeting the user
print("Good Luck!",name)

#list of words and choosing a random word
words=["raindow","computer","science","programming","python","mathematics","player","condition","reverse","water","board","geeks"]

word=random.choice(words) #selecets a random word from the words list

print("Guess the characters") #promting useer to guess

guesses="" 
turns=12
