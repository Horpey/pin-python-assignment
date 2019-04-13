# Author:: Tha UI Guy

import random

# Funtion to Load Words
def load_words():
    with open('dictionary.txt') as word_dict:
        valid_words = set(word_dict.read().split())
    return valid_words

# Get Random Word from in Dictionary
def getRandomWord():
    newList = list(set(english_words))
    randomKey = random.randint(0,len(newList))
    return newList[randomKey]
    
# Call Word Dictionary
english_words = load_words()
score = 0

# Call Random Word Function
randomWord = getRandomWord()

# print (randomWord)
shuffledWord = list(randomWord)

# Shuffle Random Word
random.shuffle(shuffledWord)
shuffledWord = ''.join(shuffledWord)
# print(shuffledWord)

# Game Display
print ('\n*************************')
print ('Python Word Game')
print ('*************************')
print ('Instruction: Reshuffle World to form a Correct Word and Earn Points\n')

print('*** '+shuffledWord+' ***\n')

# Retrieve User Word
formWord = input ('Form a Word and Press Enter\n')

# Function to Check Word in Dictionary
def checkWord():
    if (formWord in english_words):
        print ('Word Correct')
    else:
        print ('Word not Found in Dictionary')

# print(shuffledWord.find(formWord))

# CheckWord if included in Shuffled Word
if (shuffledWord.find(formWord) == -1 ):
    if (len(formWord) == len(shuffledWord)):
        checkWord()
    else: 
        print ('Oops, Word not Allowed!')
else:
    checkWord()
