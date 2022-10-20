"""
file: hashtable.py
description: open addressing Hash Table for CS 141 Lecture
language: python3.7
author: RIT CS Instructors
author: Kevin Augustine
"""

from dataclasses import dataclass
from typing import Any, Hashable, Callable

@dataclass
class HashTable:
    """
        The HashTable data structure contains a collection of values
        where each value is located by a hashable key.
        No two values may have the same key, but more than one
        key may have the same value.
        table is the list holding the hash table
        size is the number of elements in occupying the hash table
    """
    table: list
    size: int
    capacity: int
    hash_func: Callable[[Hashable],int] # a function of (Hashable) -> int

@dataclass
class Entry:
    """
       A class used to hold key/value pairs.
    """
    key: Hashable
    value: Any



def create_hash_table(hash_function, capacity):
    """
    create_hash_table: (Func : KT -> NatNum) NatNum? -> HashTable
    """
    if capacity < 2:
        capacity = 2
    table=[]
    for i in range(capacity):
        table.append(None)
    aHashTable = HashTable( table, 0, capacity, hash_function)
    return aHashTable


def hash_table_to_str(hashtable):
    """
    hash_table_to_str: HashTable -> String
    """
    result = ""
    for i in range(hashtable.capacity):
        e = hashtable.table[i]
        if not e == None:
            result += str(i) + ": "
            result += entry_to_str(e) + "\n"
    return result


def entry_to_str(entry):
    """
    entry_to_str: Entry -> String
    return the string representation of the entry.
    """
    return "(" + str(entry.key) + ", " + str(entry.value) + ")"


def keys(hTable):
    """
    keys: HashTable(K, V) -> List(K)
    Return a list of keys in the given hashTable.
    """
    result = []
    for entry in hTable.table:
        if entry != None:
            result.append(entry.key)
    return result

def has(hTable, key):
    """
    has: HashTable(K, V) K -> Boolean
    Return True iff hTable has an entry with the given key.
    """
    index = hTable.hash_func( key ) % hTable.capacity
    startIndex = index  # We must make sure we don't go in circles.
    while hTable.table[ index ] != None and hTable.table[ index ].key != key:
        index = (index + 1) % hTable.capacity
        if index == startIndex:
            return False
    return hTable.table[ index ] != None

def put(hTable, key, value):
    """
    put: HashTable(K, V) K V -> Boolean

    Using the given hash table, set the given key to the
    given value. If the key already exists, the given value
    will replace the previous one already in the table.
    If the table is full, an Exception is raised.
    """
    
    if hTable.size / hTable.capacity > 0.75:
        # Resize the hash table if the load is greater than 75%
        resize_hash_table(hTable)
    index = hTable.hash_func( key) % hTable.capacity
    startIndex = index  # We must make sure we don't go in circles.
    while hTable.table[ index ] != None and hTable.table[ index ].key != key:
        index = (index + 1) % hTable.capacity
        if index == startIndex:
            raise Exception("Hash table is full.")
    if hTable.table[ index ] == None:
        hTable.table[ index ] = Entry(key, value)
        hTable.size += 1
    else:
        hTable.table[ index ].value = value
    return True

def get(hTable, key):
    """
    get: HashTable(K, V) K -> V

    Return the value associated with the given key in
    the given hash table.

    Precondition: has(hTable, key)
    """
    index = hTable.hash_func(key) % hTable.capacity
    startIndex = index  # We must make sure we don't go in circles.
    while hTable.table[ index ] != None and hTable.table[ index ].key != key:
        index = (index + 1) % hTable.capacity
        if index == startIndex:
            raise Exception("Hash table does not contain key.")
    if hTable.table[ index ] == None:
        raise Exception("Hash table does not contain key:", key)
    else:
        return hTable.table[ index ].value

def resize_hash_table(hTable:HashTable):
    """resize_hash_table doubles the capacity of the hash table whenever the load is greater than 75 percent and rehashes each Entry
        hTable: the hash table being resized
        table: the original table in the hash table
    """

    table = hTable.table[:]     #Create the original table

    hTable.table = []
    for _ in range(hTable.capacity * 2):
        #Resets the table in the hash table to a table of Nones with a size twice of the capacity
        hTable.table.append(None)

    hTable.capacity = hTable.capacity * 2   #Change capacity
    hTable.size = 0     #Reset size

    for entry in table:
        #Iterate through each value in the table
        if entry is not None:
            #If it is an actual Entry then put it into the new hash table
            put(hTable, entry.key, entry.value)