

import random
word_list = ["ardvark", "baboon", "camel"]
choosen_word = random.choice(word_list)
word_length = len(choosen_word)

print(f"pssst, the solution is:  {choosen_word}")

display = []
for _ in range(word_length):
    display += "_"


end_of_game = False
while not end_of_game:
 guess = input("Guess a letter: ").lower()



 for position in range(word_length):
     letter = choosen_word[position]
     print(f"Current position: {position} \n current letter: {letter} \n Guessed letter: {guess}")
     if letter == guess:
        display[position] = letter
   
 print(display)

if "_" not in display:
   end_of_game = True
   print("YOU WIN!")