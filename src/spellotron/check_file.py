"""
file: check_file.py
description: Goes through the list of lines and fixes all of the words
language: python3.7
author: Kevin Augustine
"""
from spell_check import *
from printing import *

def check_file(list_of_lines:list, mode_words:bool):
    """check_file goes through each line and each word and fixes each word
        list_of_lines: a list of lines that need to be corrected
        mode_words: a boolean, True if mode is words, False if mode is lines
        dictionary: the set with the dictionary in it
        word_count: the amount of words in the file
        corrected_words: the list of uncorrected words that were corrected
        uncorrected_words: the list of uncorrected words that were never corrected
        list_of-words: list of words in each line
        word_object: the Word object with the word information in it
    """
    dictionary = make_dictionary()   #Make dictionary
    word_count = 0
    corrected_words = []
    uncorrected_words = []
    for line in list_of_lines:
        #Iterate through each line in the list
        list_of_words = []
        for word in line.strip().split():
            #Iterate through each in word in the line , fix word, increase word count, add to lists
            word_count += 1    #Increase word count
            
            word_object = make_word_object(word)   #Make word_object
            spellcheck(word_object,dictionary)     #Spellcheck word
            if mode_words is True and word_object.correct is True:
                #If the mode is words and the word is already correct, continue to the next word
                continue

            if word_object.corrected_word is not None and word_object.correct is not True:
                #If the word was corrected append the uncorrected word to the corrected word list
                corrected_words.append(word_object.uncorrected_word)
                if mode_words is True:
                    #If the mode is words then print the word in words mode and continue to the next word
                    print_words(word_object)
                    # continue
            elif word_object.correct is False and has_letters(word_object.uncorrected_word) is True:
                #If the word wasn't corrected, isn't already correct, and has at least one letter in it, append to the uncorreced word list
                uncorrected_words.append(word_object.uncorrected_word)

            list_of_words.append(word_object)   #Append the word_object to the list of words
        if mode_words is False:
            #If the mode is lines, print the line in lines mode
            print_lines(list_of_words)
    corrected_words.sort()     #Sort the corrected words list
    uncorrected_words.sort()    #Sort the uncorrected words list
    print_bottom(word_count,corrected_words,uncorrected_words)   #Print the word count, and two lists