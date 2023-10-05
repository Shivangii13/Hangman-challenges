word_list = ["ardvark", "baboon", "camel"]

#TODO-1 - randomly choose a word from the word_list and assign it to a 
# vaiable called choosen_word.

import random
choosen_word = random.choice(word_list)

#TODO-2- ask the user to guess a letter and assign their answer 
#to a variable called guess . Make guess lowercase.

guess = input("Guess a letter: ").lower()

#TODO-3- check if  the letter the user guessed is one of the 
#letter in the choosen word

for letter in choosen_word:
    if letter == guess:
        print("RIGHT")
    else:
        print("WRONG")
