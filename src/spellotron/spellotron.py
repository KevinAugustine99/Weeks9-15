"""
file: spellotron.py
description: The spellchecker
language: python3.7
author: Kevin Augustine
"""
from check_file import *


def input_main() -> (list, bool):
    """input_main takes the input from the command line and returns list of lines and words_mode
        list_of_lines: a list of lines that need to be corrected
        mode_words: True if mode is words, False if mode is lines
    """
    if len(argv) == 1 or (argv[1] != "lines" and argv[1] != "words"):
        #If the command line was inputted incorrectly, print the error and quit
        print_error()
        exit()

    if len(argv) <= 2:
        #If the command line doesn't have the text file parameter, put the stdin in the the list_of_lines
        list_of_lines = [stdin.readline()]
    else:
        #If the command line does have a text file parameter, read file and make the list of lines
        list_of_lines = read_file(argv[2])

    if argv[1] == "words":
        #If mode is words, mode_words is True
        mode_words = True
    else:
        #Else mode_words is False
        mode_words = False
    
    return (list_of_lines, mode_words)

def main():
    (list_of_lines, mode_words) = input_main()
    check_file(list_of_lines, mode_words)

if __name__ == "__main__":
    main()