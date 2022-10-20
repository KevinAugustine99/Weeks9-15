"""
file: test_link_sort.py
author: your name here
description: tester for functions in linked_insort.py
"""

import linked_insort as ls
import linked_code as lc


def read_file( fname ):
    """
       Open a file of containing one integer per line,
       prepend each integer to a linked sequence,
       and return the reverse of the sequence.
       :param fname: A string containing the name of the file
       :return: A linked list of the numbers in the file, ordered
                identically to how they are ordered in the file
        originals: the linked list from the file in the opposite order than the file
    """
    originals = None
    for line in open(fname):
        #For each file in the file it appends each new value
        originals = lc.LinkNode( int(line.strip()), originals)
    
    return lc.reverse_tail_rec(originals)

def main():
    """
       Read file, build sequence, print it, sort it, print result, and
       pretty-print both lists.
    """

    name = input( "Enter file name: " )    
    if name == "":
        return
    original_s = read_file( name )
    print( "unsorted:", original_s)

    sorted_s = ls.insort( original_s )

    print( "sorted:", sorted_s )

    print( "pretty printed original: ", end="")
    ls.pretty_print( original_s )
    print( "pretty printed sorted: ", end="")
    ls.pretty_print( sorted_s )



if __name__ == "__main__":
    main()
