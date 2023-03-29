import random
import string
from hang_draw import lives_visual_dict
from words import words

def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.lower()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_lowercase)
    used_letters = set()  # what the user has guessed

    lives_left = 7

    # getting user input
    while len(word_letters) > 0 and lives_left > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives_left, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives_left])
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').lower()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives_left = lives_left - 1  # takes away a life if wrong
                print('\n', 'Your letter,', user_letter, 'not in the word.')

        elif user_letter in used_letters:
            print('\n', 'Used letter. Guess again.')

        else:
            print('\n','Not a valid letter.')

    #ä here when len(word_letters) == 0 OR when lives == 0
    if lives_left == 0:
        print(lives_visual_dict[lives_left])
        print('The man is Hanged!! The word is:', word)
    else:
        print('YAY! You guessed the word', word, '!!')


if __name__ == '__main__':
    hangman()