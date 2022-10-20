"""
File : selection_sort.py
Assignment : HW #7
Language : python3
Author : Kevin Augustine < kea4437@rit.edu >
"""

def task1():
    """task_1 reads and stores the american-english file into a dictionary where the keys are the anagrams and the values are all the words that fit the anagram and returns the dictionary.
        dict_anagram: the dictionary where the keys are anagrams and the values are the words that fot the anagram
        line: each line in the american-english text file
        unsorted_list: the unsorted list of characters in the line
        anagram: the sorted anagram
    """
    dict_anagram = {}
    for line in open("american-english.txt", encoding="utf-8"):
        unsorted_list = list(line.strip())
        unsorted_list.sort()
        anagram = ''.join(unsorted_list)
        if not anagram in dict_anagram.keys():
            #If the anagram is unique, creates a key-value new pair in the dictionary
            dict_anagram[anagram] = [line.strip()]
        else:
            #If the anagram is not unique, adds a new value to an existing key-value pair
            dict_anagram[anagram].append(line.strip())
    return dict_anagram
        
def task2(dict_anagram, input_word):
    """task2 askes for a string and prints all of the words in the dictionary that uses the input string as an anagram.
        dict_anagram: the dictionary where the keys are anagrams and the values are the words that fot the anagram
        input_word: the input string from the user
        unsorted_list: the unsorted list of characters in the input_word
        anagram: the sorted anagram for input_word
    """
    
    unsorted_list = list(input_word)
    unsorted_list.sort()
    anagram = ''.join(unsorted_list)
    if not anagram in dict_anagram.keys():
        #Runs if the anagram for the input_word doesn't exist in the dictionary
        print("No words can be formed from: " + input_word)
    else:
        #Prints the corresponding words for the input_word
        print("Corresponding words: ",dict_anagram[anagram])

def task3(dict_anagram, word_length):
    """task3 inputs a word length and identifies and prints the maximum size list of American English words that are the same length as the inputed word length that are all anagrams of each other.
        dict_anagram: the dictionary where the keys are anagrams and the values are the words that fot the anagram
        word_length: the inputed word length
        max_length: the length of the largest list
        max_key: the key anagram of the largest list
        key: the keys in the dictionary
    """
    max_length = 0
    max_key = ""
    for key in dict_anagram:
        #Runs through each key in the dictionary
        if len(key) == int(word_length):
            #Checks to see if the length of the key is the same length of the inputed word
            if len(dict_anagram[key]) > max_length:
                #If the length of the current list is greater than the length of the largest list so far then the max_length become the length of the current list and changes the key to the key of the current list
                max_length = len(dict_anagram[key])
                max_key = key
    print("Max anagrams for length " + word_length + ":", max_length)
    print("Anagram list:",dict_anagram[max_key])

def task4(dict_anagram,word_length):
    """task4 inputs a word length and how many words of inputed length in the dictionary have unique anagrams.
        dict_anagram: the dictionary where the keys are anagrams and the values are the words that fot the anagram
        word_length: the inputed word length
        count: count of how many words of inputed length in the dictionary have unique anagrams
        key: the keys in the dictionary
    """
    count = 0
    for key in dict_anagram:
        #Runs through each key in the dictionary
        if len(key) == int(word_length):
            #Checks to see if the length of the key is the same length of the inputed word
            if len(dict_anagram[key]) == 1:
                #Increases the count if the anagram is unique (list of that key = 1)
                count += 1
    print("Number of jumble usable words of length " + word_length + ":", count)

def main():
    dict_anagram = task1()
    while True:
        input_word = input("Enter input string (hit enter key to go to task 3):")
        if input_word == "":
            #Breaks loop if user inputs an empty string
            break
        task2(dict_anagram,input_word)
    print("\n")
    while True:
        word_length = input("Enter word length (hit enter key to go to task 4):")
        if word_length == "":
            #Breaks loop if user inputs an empty string
            break
        task3(dict_anagram,word_length)
    print("\n")
    while True:
        word_length = input("Enter word length (hit enter key to quit):")
        if word_length == "":
            #Breaks loop if user inputs an empty string
            break
        task4(dict_anagram,word_length)

if __name__ == "__main__":
    main()


