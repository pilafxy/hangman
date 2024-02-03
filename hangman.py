import random
import sys

word_list = []

with open("word_list.txt") as f:
    for line in f:
        this = (line[0: -1].lower())
        word_list.append(this)


def check(x):
    if x in current_guess:
        return True
    else:
        return False


def print_out(string):
    for i in string:
        print(i, end=" ")
    print('\n')
    if '_' not in current_guess:
        print('Congratulation!\nYou have solved the puzzle!')
        sys.exit(0)


def guess():
    raw = input('Letter: ')[0]
    letter = raw.lower()
    if check(letter):
        print(letter, 'was already entered.')
    if letter in word:
        solution(letter)
    elif letter not in word:
        dead(counter)
    else:
        print('else')


def solution(value):
    for i in range(len(word)):
        if word[i] == value:
            current_guess.insert(i, value)
            replace = i + 1
            del current_guess[replace]
    print('\n')
    print_out(current_guess)
    guess()


def dead(i):
    global counter
    if i == 0:
        print("""
                  +---+
                  |   |
                      |
                      |
                      |
                      |
                =========""")
        counter += 1
        guess()
    elif i == 1:
        print("""
                  +---+
                  |   |
                  O   |
                      |
                      |
                      |
                =========""")
        counter += 1
        guess()
    elif i == 2:
        print("""
                  +---+
                  |   |
                  O   |
                  |   |
                      |
                      |
                =========""")
        counter += 1
        guess()
    elif i == 3:
        print("""
                  +---+
                  |   |
                  O   |
                 /|   |
                      |
                      |
                =========""")
        counter += 1
        guess()
    elif i == 4:
        print("""
                  +---+
                  |   |
                  O   |
                 /|\  |
                      |
                      |
                =========""")
        counter += 1
        guess()
    elif i == 5:
        print("""
                  +---+
                  |   |
                  O   |
                 /|\  |
                 /    |
                      |
                =========""")
        counter += 1
        guess()
    elif i == 6:
        print("""
                  +---+
                  |   |
                  O   |
                 /|\  |
                 / \  |
                      |
                =========""")
        print('You are dead..')


# get random word
max_value = int(len(word_list)-1)
num = random.randint(0, max_value)
word = word_list[num]
#
current_guess = []
for char in word:
    current_guess.append('_')
#
counter = 0
#
print('###HANG MAN###\n')
print('Guess the word below\n')
guess()
