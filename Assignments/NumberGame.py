# Tha UI Guy

import random
number = random.randint(0,100)
print (number)

while True:
    guess = input('Guess the Number 🤔\n')

    try:
        guessInt = int(guess)
        guessResult = int(guess)
        if guessResult == number:
            print ('Got it Correct!')
            break
        else:
            print ('Oops, You got it Wrong!')

    except ValueError:
        print ('Nonvalid Input, Please input a Number')



