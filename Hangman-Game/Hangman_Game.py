import random
from collections import Counter

someWords='''apple banana mango strawberry orang grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon'''
someWords-someWords.split('')

word = random.choice(someWords)

if __name__ == '__main__':
    print('Guess the word! HINT:word is a fruit.')

    for _ in word:
        print('_',end='')
    print()

    letterGuessed=''
    chances = len(word)+2
    flag=0

    try:
        while chances > 0 and flag == 0:
            print()
            chances-=1
    except KeyboardInterrupt:
        print('\n Game Interrupted. Bye!')
        exit()