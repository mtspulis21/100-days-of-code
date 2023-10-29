#todo 1 

import random
end_of_game = False
word_list = ['pedir','avisar','gorjeta']
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display =[]
lives = 6
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Test the word and its variables
# print(chosen_word)

for letter in range(word_length):
    display += '_'

while not end_of_game:
    guess = str(input('Choose a letter: ')).lower()
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('You lost.')
            print(f'The word was: {chosen_word}')
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print('You won!') 
    print(stages[lives]) 
