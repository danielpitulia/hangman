#!/usr/bin/env python3

# Hangman for programmers!
# This script is a short hangman game written in Python. I wrote it for learning
# Python.
# /Daniel Pitulia

import random
import re

alternatives = ["javascript","python", "bash", "perl", "github", "raspberrypi"]
count_fail = 0
hangman = """\
###########################
    #              ##
    O              ##
   \|/             ##
    |
   / \             ##
                   ##
                   ##
                   ##
"""

# Randomly choose a word from the list of alternatives
answer = alternatives[random.randrange(0,len(alternatives))]	# String of answer
answer_remaining = list(answer)		# List of answer

# Define progress line: starts with for example " _ _ _ _ _" if the word
# has 5 characters

progress = "_"*len(answer)
progress = list(progress)

indx_matches = []

print("Welcome to Hangman for programmers!\n Guess the following word using lowercase: ",
"".join(progress), "\n Guess a character :)")

# While progress is not completed, prompt a guess, use re.finditer to find matches
# and store these in indx_matches.

def find_matches_and_save(guess, answer):
	global indx_matches

	""" Search guess in answer using re.finditer, find indexes, remove succesful
	guess from answer_remaining[], add succesful guess to progress[] and return
	answer_remaining[] and progress[]"""

	matches = re.finditer(guess, answer)


	for m in matches:
		indx_matches.append(m.span()[0]) # Store index of match from m.span()[0]

	# Save result

	for indx in indx_matches:
		answer_remaining[indx] = ""	# Removes correct guess from answer_remaining
		progress[indx] = guess	# Adds correct guess to the progress list

	return answer_remaining, progress

def print_result(answer_is):
	global count_fail	# Not sure about the correct way of including count_fail. I used global.
	if answer_is == "correct":
		print(hangman + "\n Correct guess: " + guess + "".join(progress))
	else:
		count_fail +=1
		print(hangman + "\n Failed guess: " + guess + "\n" + "Times failed: " + str(count_fail))
	return count_fail

while "_" in progress:
	guess = input()
	if guess in answer:
		find_matches_and_save(guess, answer)
		print_result("correct")
	else:
		print_result("fail")
