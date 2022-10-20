"""
file: helper_functions.py
description: Has all of the helper functions, and global variables
language: python3.7
author: Kevin Augustine
"""
from dataclasses import dataclass
from typing import Union
from sys import argv, stderr, stdin

LEGAL_WORD_FILE = "american-english.txt"   #The dictionary text file
KEY_ADJACENCY_FILE = "keyboard-letters.txt"   #The adjacent keys text file
ALPHABET = tuple( chr( code ) for code in range( ord( 'a' ), ord( 'z' ) + 1 ) )   #Tuple with whole alphabet

@dataclass
class Word:
    """
    An object to hold each word
    """
    uncorrected_word: str   #The original uncorrected word
    corrected_word: Union[str,None]    #The word after it gets corrected
    puncuation_before: Union[str,None]  #The puncuation before the word
    puncuation_after: Union[str,None]   #The puncuation after the word
    capitalized: bool   #True if the first letter is capitalized
    correct: bool   #True if the word is correct before correction

def make_word_object(word: str) -> Word:
    """make_word_object takes a word(string) and makes a Word object out of it
        precondition: word has no spaces in it
        word: the string which was the word turning into the Word object
        word_object: the Word object
        return: word_object
    """
    word_object = Word(word,None,"","",False,False)
    while has_punctuation(word_object.uncorrected_word[0]) == True and len(word_object.uncorrected_word) > 1:
        #While the beginning of the word is punctuation, it adds the puncuation to puncuation before and removes it from uncorrected word 
        word_object.puncuation_before = word_object.puncuation_before + word_object.uncorrected_word[0]
        word_object.uncorrected_word = word_object.uncorrected_word[1:]
    while has_punctuation(word_object.uncorrected_word[-1]) == True and len(word_object.uncorrected_word) > 1:
        #While the end of the word is punctuation, it adds the puncuation to puncuation after and removes it from uncorrected word 
        word_object.puncuation_after =  word_object.uncorrected_word[-1] + word_object.puncuation_after
        word_object.uncorrected_word = word_object.uncorrected_word[0:-1]
    if word_object.uncorrected_word[0].isupper():
        #If the first letter is uppercase, set the word_object.capitalized to True
        word_object.capitalized = True
    return word_object

def make_dictionary() -> set:
    """make_dictionary makes and returns a set with the whole dictionary in it
        dictionary: the set with the whole dictionary in it
        return: dictionary
    """
    dictionary = set()
    with open(LEGAL_WORD_FILE, encoding="utf-8") as file2:
        #Open the dictionary file as file2
        for line in file2:
            #For each line(word) in the file add it to the set
            dictionary.add(line.strip())
    return dictionary

def make_dictionary_adjacent_keys() -> dict:
    """make_dictionary_adjacent_keys makes and returns a dictionary with all of the adjacent keys in it
        adjacent_keys: the dictionary with all of the adjacent_keys in it
        adjacent_keys.key: the key being pressed
        adjacent_keys.value: the values next to the key
        return: adjacent_keys
    """
    adjacent_keys = {}
    with open(KEY_ADJACENCY_FILE, encoding="utf-8") as file3:
        #Open the adjacent keys file as file3
        for line in file3:
            #For each line in the file add it to the adjacent_keys dictionary
            letters = line.strip().split()
            adjacent_keys[letters[0]] = letters[1:]
    return adjacent_keys


def read_file(file_name:str) -> list:
    """read_file makes and returns a list with all of the lines in the file
        file_name: the name of the file being read (str)
        list_of_lines: a list of all of the lines in the file
        return: list_of_lines
    """
    list_of_lines = []
    with open(file_name) as file1:
        #Open the file as file1
        for line in file1:
            #For each line in the file add it to the list of lines
            list_of_lines.append(line.strip())
    return list_of_lines

def has_punctuation(word: str ) -> bool:
    """has_punctuation returns true if the word has any puncutation in it
        word: the word being checked for puncuation
        return: bool
    """
    for x in word:
        #Iterate through each character in the word
        if x == "_" or x.isidentifier() is False:
            #If the character is puncuation then return True
            return True
    return False

def check_valid(word: str) -> bool:
    """check_valid checks if the word is valid for method one of spellchecking
        return: bool
        True: if it is valid
        False: if it is not valid
    """
    adjacent_keys = make_dictionary_adjacent_keys()
    for x in word:
        #Iterate through each character in the word
        if x not in adjacent_keys.keys():
            #If the character is puncuatuion or uppercase return False
            return False
    return True

def has_letters(word:str) -> bool:
    """has_letters checks if a word has a letter and returns True if it does
    """
    for x in word:
        #Iterate through each character in the word
        if x.isidentifier() is True and x != "_":
            #If the character is a letter return True
            return True
    return False