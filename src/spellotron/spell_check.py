"""
file: spell_check.py
description: Has all methods of spellchecking and spell checks one word
language: python3.7
author: Kevin Augustine
"""
from helper_functions import *

def method_one(word_object: Word, dictionary: set):
    """method_one uses the first method to spellcheck the word
        misspelling method: misspelling due to hitting an adjacent key
        method of fixing: For each of the n letters, the program should try alternatives in the order 
        they are listed in the key file. The first time a legal word is found this way, checking is done; return the fixed word.

        word_object: the Word object with the word information in it
        dictionary: the set with the dictionary in it
        mutable_list: the list of characters of the word
        adjacent_keys: the dictionary of adjacent keys
    """
    mutable_list = list(word_object.uncorrected_word[:])
    adjacent_keys = make_dictionary_adjacent_keys()
    for idx in range(len(mutable_list)):
        #Iterate through each index in the mutable list
        original_letter = mutable_list[idx]     #Set original letter to the letter at that index
        for x in adjacent_keys[mutable_list[idx]]:
            #For each adjacent key to the current character
            mutable_list[idx] = x   #Set that index to the adjacent key
            possible_word = "".join(mutable_list)   #Join the list together to make the possible word
            if possible_word in dictionary:
                #If the possible word is in the dictionary set the possible word to the corrected word and return
                word_object.corrected_word = possible_word
                return
            else:
                #If the possible word is not in the dictionary set the character back and continue iterating through the word
                mutable_list[idx] = original_letter
        
def method_two(word_object: Word, dictionary: dict):
    """method_two uses the second method to spellcheck the word
        misspelling method: misspelling due to failing to type one key
        method of fixing: For each of the n + 1 intercharacter positions in w, the program should try 
        inserting one of the 26 letters of the English alphabet at that position. Letters are tried in alphabetical order

        word_object: the Word object with the word information in it
        dictionary: the set with the dictionary in it
        mutable_word: the word being mutated
        possible_word: a possible word that could be in the dictionary
        x: letter in alphabet
        ALPHABET: the alphabet in a tuple
    """
    mutable_word = word_object.uncorrected_word[:]
    for i in range(len(mutable_word)+1):
        #Iterate through each position in the word
        for x in ALPHABET:
            #Iterate through each letter in the alphabet
            possible_word = mutable_word[0:i] + x + mutable_word[i:]    #Possible word is created by inserting the letter in the current spot in the word
            if possible_word in dictionary:
                #If the word is in the dictionary set the corrected word to the possible word and return
                word_object.corrected_word = possible_word
                return

def method_three(word_object: Word, dictionary: dict):
    """method_three uses the third method to spellcheck the word
        misspelling method: misspelling due to typing an extra key
        fixing method: For each of the n letters, the program should try deleting that letter. 
        The first time a legal word is found this way, checking is done; return the fixed word.

        word_object: the Word object with the word information in it
        dictionary: the set with the dictionary in it
        mutable_word: the word being mutated
        possible_word: a possible word that could be in the dictionary
    """
    mutable_word = word_object.uncorrected_word[:]
    if len(mutable_word) == 1:
        return
    for i in range(len(mutable_word)):
        #Iterate through each position in the word
        possible_word = mutable_word[0:i] + mutable_word[i+1:]    #Delete the letter at that position
        if possible_word in dictionary:
            #If the word is in the dictionary set the corrected word to the possible word and return
            word_object.corrected_word = possible_word
            return




def fix_word(word_object: Word, dictionary: dict):
    """fix_word tries to fix the word by using the three methods
        word_object: the Word object with the word information in it
        dictionary: the set with the dictionary in it
    """
    if check_valid(word_object.uncorrected_word):
        #If the word could run through method one without failing, run method one
        method_one(word_object,dictionary)
    if word_object.corrected_word is None:
        #If the word isn't corrected run method two
        method_two(word_object,dictionary)
    else:
        #If the word was corrected, return
        return

    if word_object.corrected_word is None:
        #If the word isn't corrected run method 3 
        method_three(word_object,dictionary)


def spellcheck(word_object: Word ,dictionary: dict):
    """spellcheck spell checks the word
        word_object: the Word object with the word information in it
        dictionary: the set with the dictionary in it
    """
    if word_object.uncorrected_word.isdigit():
        #If the word is a number then return
        return

    if word_object.uncorrected_word not in dictionary:
        #If the word is not in the dictionary, fix word
        fix_word(word_object,dictionary)
        if word_object.capitalized is True:
            #If the word is capitalized uncapitalize the first letter
            word_object.uncorrected_word = word_object.uncorrected_word[0].lower() + word_object.uncorrected_word[1:] 
            if word_object.uncorrected_word not in dictionary:
                #If the word is not in the dictionary, fix word
                fix_word(word_object,dictionary)
            else:
                #If the word is correct set word_object.correct = True
                word_object.correct = True
    else:
        #If it was not corrected and the word is correct set word_object.correct = True
        word_object.correct = True
    
    if word_object.capitalized is True:
        #If the first letter was capitalized then capitalize the first letter of the uncorrected word
        word_object.uncorrected_word = word_object.uncorrected_word[0].upper() + word_object.uncorrected_word[1:]
        if word_object.corrected_word is not None:
            #If the corrected word is not None then capitalize the first letter of the corrected word
            word_object.corrected_word = word_object.corrected_word[0].upper() + word_object.corrected_word[1:]

    #Put the punctuatiuon back onto the uncorrected word and corrected word
    word_object.uncorrected_word = word_object.puncuation_before + word_object.uncorrected_word + word_object.puncuation_after
    if word_object.corrected_word is not None:
        #If corrected word is not None
        word_object.corrected_word = word_object.puncuation_before + word_object.corrected_word + word_object.puncuation_after
    