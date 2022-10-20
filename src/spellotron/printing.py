"""
file: printing.py
description: Has all of the printing functions and does all of the printing
language: python3.7
author: Kevin Augustine
"""
from helper_functions import *

def print_words(word_object: Word):
    """print_words prints the word in words mode
        word_object: the word object with the word in it
    """
    print(word_object.uncorrected_word + " -> "+ word_object.corrected_word)

def print_lines(list_of_words: list):
    """print_lines prints the words in lines mode
        list_of_words: the list of word objects in each line 
    """
    for word_object in list_of_words:
        #Iterate through each word in the list of word object
        if word_object.corrected_word is not None:
            #If the word was corrected print the corrected word
            print(word_object.corrected_word, end=" ")
        else:
            #If the word wasn't corrected print the uncorrected word
            print(word_object.uncorrected_word,end=" ")
    print("\n",end="")

def print_bottom(word_count: int, corrected_words:list, uncorrected_words:list):
    """print_bottom prints the stats of the file at the bottom
        word_count: the amount of words in the file
        corrected_words: the list of corrected words
        uncorrected_words: the list of uncorrected words
    """
    print("\n")
    print(word_count,"words read from file.")
    print("\n")
    print(len(corrected_words),"Corrected Words")
    print(corrected_words)
    print("\n")
    print(len(uncorrected_words),"Unknown Words")
    print(uncorrected_words)

def print_error():
    """print_error prints the error message
    """
    print("Usage: python3.7 spellotron.py words/lines [filename]", file = stderr)

