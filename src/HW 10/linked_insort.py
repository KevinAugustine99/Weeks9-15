"""
file: linked_insort.py
author: Kevin Augustine
description: homework
"""

import linked_code as lc


def insert( value, lnk ):
    """
    Put the value in the proper spot in the linked list to keep it sorted.
    New nodes are created.
    :param value: the value to add to the sequence of values in the list
    :param lnk: the node at the head of the list
    :return: a (partially) new linked list with the value inserted
    :pre: the list headed by lnk is sorted.
    :post: the link returned refers to a list that is sorted.
    """
    if lnk is None:
        #If the value is the greatest value so far, it will return a Node with a value: inserted value and the rest: None
        return lc.LinkNode(value,None)
    elif value < lnk.value:
        #If the value being inserted is less than the next value in the sorted list then it returns a Node with a value: inserted value and the rest: the rest of lnk
        return lc.LinkNode(value, lnk)
    else:
        #If the value being inserted is greater then the next value in the sorted list then it returns a node witha vlue of the current value in lnk and the rest is recursively calling itself, because it is still inserting the insertion value
        return lc.LinkNode(lnk.value, insert(value, lnk.rest))

def insort( lnk):
    """
    Return a copy of a linked list where all the values are sorted,
    with the lowest value at the head.
    :param lnk: the node at the head of the provided list
    :return: the head node of the sorted linked list
    sorted_link: the new sorted link
    """
    sorted_link = None

    while lnk != None:
        #Iterates through each value in lnk and inserting each value into the sorted link
        sorted_link = insert(lnk.value, sorted_link)
        lnk = lnk.rest
    return sorted_link



def pretty_print( lnk ):
    """
    Print the contents of a linked list in standard Python format.
    [value, value, value] (Note the spaces.)
    :param lnk: the node at the head of the provided list
    :return: None
    """
    print("[", end='')
    if lnk == None:
        #If the link is empty then it prints an empty list
        print("]")
    else:
        while lnk != None:
            #Iterates through each value in lnk
            if lnk.rest is None:
                #If value is the last value, then it prints the value and the close bracket without the comma and the space
                print(str(lnk.value)+"]")
            else:
                #If the value isn't the last value then it prints the value, a comma, and a space
                print(str(lnk.value)+",",end=' ')
            lnk = lnk.rest