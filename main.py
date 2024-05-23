from random import choices
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
colorama_init()

with open("corncob.txt") as f:
    all_wordlist = set(word.strip() for word in f.readlines())

def valid_word(word):
    if len(word) < 4:
        return False
    has_main_letter = False
    for letter in word:
        if letter not in letters:
            return False
        if letter == letters[0]:
            has_main_letter = True
    if not has_main_letter:
        return False
    return True

max_score = 0
while max_score == 0:
    letters = choices('abcdefghijklmnopqrstuvwxyz', k=7)
    wordlist = set(filter(valid_word, all_wordlist))
    max_score = sum(map(len, wordlist))

score = 0
guessed_words = []
print(f"Letters: {Fore.RED+letters[0]+Style.RESET_ALL}, {', '.join(letters[1:])}")
print(f"Max possible score: {max_score}")

while score < max_score:
    guess = input('')
    if guess not in wordlist:
        print(f"{guess} is not in the wordlist")
        continue
    if guess in guessed_words:
        print(f"{guess} has been guessed")
        continue
    if len(guess) < 4:
        print(f"{guess} is too short")
    valid = True
    has_main_letter = False
    for letter in guess:
        if letter not in letter:
            print(f"'{letter}' is not allowed")
            valid = False
        if letter == letters[0]:
            has_main_letter = True
    if valid and has_main_letter:
        score += len(guess)
        guessed_words.append(guess)
        print(f"Score: {score}")