word_list = ["ardvark", "baboon", "camel"]

import random
choosen_word = random.choice(word_list)

print(f"pssst, the solution is:  {choosen_word}")

display = []
word_length = len(choosen_word)
for _ in range(word_length):
    display += "_"
print(display)



guess = input("Guess a letter: ").lower()



for position in range(len(choosen_word)):
    letter = choosen_word[position]
    if letter == guess:
        display[position] = letter
   
print(display)

