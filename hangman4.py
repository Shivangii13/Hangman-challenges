import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
 '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
'''
 +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', 
 '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
'''
  +---+
  |   |
      |
      |
      |
      |
=========''', ]
end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
choosen_word = random.choice(word_list)
word_length = len(choosen_word)

print(f"pssst, the solution is:  {choosen_word}")

display = []
for _ in range(word_length):
    display += "_"



while not end_of_game:
  guess = input("Guess a letter: ").lower()



  for position in range(word_length):
     letter = choosen_word[position]
    # print(f"Current position: {position} \n current letter: {letter} \n Guessed letter: {guess}")
     if letter == guess:
        display[position] = letter
  lives = 6
  if guess not in choosen_word:
    lives -= 1
    if lives == 0:
     end_of_game = True
     print("you lose!")

print(f"{' '.join(display)}")
   
 
if "_" not in display:
   end_of_game = True
   print("YOU WIN!")

print(stages[lives])