#!/usr/bin/env python3

# Hangman for programmers!
# This script is a short hangman game written in Python. I wrote it for learning
# Python.
# /Daniel Pitulia

import random
import re

alternatives = ["javascript"]
count_fail = 0

hangman = [
    "\t O\t\t##",
    "\t\|/\t\t##",
    "\t | \t\t##",
    "\t/ \ \t\t##",
]

hang_pole = [
    "###########################",
    "\t #\t\t##",
    "\t\t\t##",
    "\t\t\t##",
    "\t\t\t##",
    "\t\t\t##",
    "\t\t\t##",
    "\t\t\t##",
    "\t\t\t##",
]
# Randomly choose a word from the list of alternatives
answer = alternatives[random.randrange(0,len(alternatives))]	# String of answer
answer_remaining = list(answer)		# List of answer

# Define progress line: starts with for example " _ _ _ _ _" if the word
# has 5 characters

progress = "_"*len(answer)
progress = list(progress)


print("Welcome to Hangman for programmers!")
for line in hang_pole:
    print(line)

print("Find the following word by guessing matching characters: ")
print("".join(progress), "\nHint: the word is a programming language. You are allowed four incorrect guesses.")

# While progress is not completed, prompt a guess, use re.finditer to find matches
# and store these in indx_matches.

def find_matches(guess, answer):
    """ Search guess in answer using re.finditer, find indexes, remove succesful
    guess from answer_remaining[], add succesful guess to progress[] and return
    answer_remaining[] and progress[]"""

    indx_matches = []
    matches = re.finditer(guess, answer)


    for m in matches:
        indx_matches.append(m.span()[0]) # Store index of match from m.span()[0]

        # Save result
    return indx_matches






while "_" in progress:
    guess = input()
    if guess in answer:
        indx = find_matches(guess, answer)
        for i in indx:
            answer_remaining[i] = ""
            progress[i] = guess


        for line in hang_pole:
            print(line)
        print("Correct guess: " + "".join(progress))
    else:
        count_fail +=1
        hang_pole[count_fail+1] = hangman[count_fail-1]

        for line in hang_pole:
            print(line)
        print("Failed guess: " + guess + "\n" + "Times failed: " + str(count_fail))

    if(count_fail > 3):
        print("Sorry, you're dead :(")
        break
