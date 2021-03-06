#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""
Mimic exercise

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read it into
one giant string and split it once.

Note: the standard python module 'random' includes a random.choice(list)
method which picks a random element from a non-empty list.

You can try adding in line breaks around 70 columns so the output looks
better.
"""

__author__ = """Bethany Folino with help from Jacob Short, Matt Perry, and
https://stackoverflow.com/questions/42602284/dictionary-containing
-words-from-a-text-file-as-keys-with-a-list-of-all-the-next"""


import random
import sys


def create_mimic_dict(filename):
    """
    Returns a dict mapping each word to a list of words which follow it.
    For example:
        Input: "I am a software developer, and I don't care who knows"
        Output:
            {
                "" : ["I"],
                "I" : ["am", "don't"],
                "am": ["a"],
                "a": ["software"],
                "software" : ["developer,"],
                "developer," : ["and"],
                "and" : ["I"],
                "don't" : ["care"],
                "care" : ["who"],
                "who" : ["knows"]
            }
    """
    with open(filename) as text:
        contents = text.read()
        contents = contents.split()
        words = {"": ["I"]}
        for i in range(len(contents) - 1):
            words.setdefault(contents[i], []).append(contents[i+1])
        words.setdefault(contents[-2], [])
        return words


def print_mimic_random(mimic_dict, num_words):
    """
    Given a previously created mimic_dict and num_words,
    prints random words from mimic_dict as follows:
        - Use a start_word of '' (empty string)
        - Print the start_word
        - Look up the start_word in your mimic_dict and get its next-list
        - Randomly select a new word from the next-list
        - Repeat this process num_words times
    Hint: `print()` automatically adds a newline unless you tell it not to.
    Look
    up the `end` keyword argument for the `print()` function.
    """
    count = 1
    while count <= num_words:
        for word in mimic_dict:
            if word == "":
                pass
            else:
                words = mimic_dict.get(word)
                randomize = random.choice(words)
                print(randomize, end=" ")
                count += 1


def main(args):
    # Get input filename from command line args
    filename = args[0]

    # Create and print the jumbled (mimic) version of the input file
    print(f'Using {filename} as input:\n')
    d = create_mimic_dict(filename)
    print_mimic_random(d, 200)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: python mimic.py file-to-read')
    else:
        main(sys.argv[1:])
    print('\n\nCompleted.')
