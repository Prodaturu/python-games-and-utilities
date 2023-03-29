import random
from words import words 
from hang_draw import lives_visual_dict

customWords=input('Want to add custom words to word pool: y/n')
if (customWords == 'y'):
  customWords=input('Enter your custom words with "," separating them: ').split(',')
  words.extend(customWords)
elif (customWords != 'y' and customWords!= 'n' ):
  print('Invalid input. Default words will be used')

#+ 1) computer picks a valid word from word pool:
def validWords(words):
  secret_word = random.choice(words) # choose random word in words list
  while '_' or ' ' in secret_word:
    secret_word = random.choice(words)
  return secret_word.lower()

#+ 2) Game Logic / code :


def hangman():
  print('This section needs more code to be written')