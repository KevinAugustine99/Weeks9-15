"""
File : dna.py
Assignment : Lab #8
Language : python3
Author : Kevin Augustine < kea4437@rit.edu >
"""
import linked_code as lc

def convert_to_nodes(dna_string):
    """convert_to_nodes takes a string of DNA nucleotides and turns it into a linknode
        return: linknode where each value is a string with a nucleotide
        dna_string: the string of DNA nucleotides
    """
    if dna_string == "":
        #When the string is over, it returns none
        return None
    else:
        #When the string isn't over, the program creates and returns a LinkNode where the value is the first value in the string and for the rest it calls itself recursively with the rest of the string
        return lc.LinkNode(dna_string[0],convert_to_nodes(dna_string[1:]))

def convert_to_string(dna_seq):
    """convert_to_string takes a LinkNode of DNA nuclotides and turns it into a string
        return: a string where each character is a DNA nucleotide
        dna_seq: the linknode where each value is a string with a nucleotide
    """
    if dna_seq is None:
        #When the linknode is over, it returns an empty string
        return ""
    else:
        #When the linknode isn't over, the program returns the concatenation of the value and recursively calls the function itself with the rest of the linknode
        return dna_seq.value + convert_to_string(dna_seq.rest)

def is_match(dna_seq1, dna_seq2):
    """is_match checks if the first sequence and the second sequence are exact matches
        dna_seq1: the first dna sequence, a linknode
        dna_seq2: the second dna sequence, a linknode
    """
    if dna_seq1 == None and dna_seq2 == None:
        #If the function goes through both linknodes and its equal at every value, then it returns True
        return True
    elif dna_seq1 == None or dna_seq2 == None or dna_seq1.value != dna_seq2.value:
        #If the two linknodes are different lengths or two values are different then the program returns False
        return False
    else:
        #If the two linknode values are equal then the program recursively calls itself with the rest of the linknodes
        return is_match(dna_seq1.rest,dna_seq2.rest)

def is_pairing(dna_seq1, dna_seq2):
    """is_pairing checks if the first sequence is an exact paired sequence to the second sequence
        dna_seq1: the first dna sequence, a linknode
        dna_seq2: the second dna sequence, a linknode
    """
    if dna_seq1 == None and dna_seq2 == None:
        #If the function goes through both linknodes and is a pair at every value, then it returns True
        return True
    elif dna_seq1 == None or dna_seq2 == None:
        #If the two linknodes are different lengths then it returns False
        return False
    elif (dna_seq1.value == "A" and dna_seq2.value != "T") or (dna_seq1.value == "T" and dna_seq2.value != "A") or (dna_seq1.value == "G" and dna_seq2.value != "C") or (dna_seq1.value == "C" and dna_seq2.value != "G"):
        #If the two linknode values are not pairs then it returns false
        return False
    else:
        #If the two linknode values are pairs then the program recursively calls itself with the rest of the linknodes
        return is_pairing(dna_seq1.rest, dna_seq2.rest)

def is_palindrome(dna_seq):
    """is_palindrome checks whether a sequence is a palindrome (Its the same when the sequence is reversed) returns True or False
        dna_seq: the sequence being checked to see if its a palindrome (a linknode)
    """
    if is_match(dna_seq,lc.reverse_tail_rec(dna_seq)) is True:
        #If the linknode and its reverse matches then it returns True
        return True
    else:
        #If the linknode and its reverse matches then it returns False
        return False

def substitution(dna_seq1,idx,base):
    """substitution substitutes one base in the dna sequance for another base at a certain index and returns that new sequence
        dna_seq1: the sequence that is getting changed (a linknode)
        idx: the index in the sequence that is being changed
        base: the new base that is being substituted in
    """
    if idx == 0:
        #When the sequence gets to the intended idex, it returns a LinkNode with the new base as the value and the rest of the original linknode, replacing the original value in that index
        return lc.LinkNode(base,dna_seq1.rest)
    elif dna_seq1 is None:
        #If it reaches the end of the sequence then an out of Index error is raised
        raise IndexError("Invalid Substitution Index")
    else:
        #If the program hasn't reached the index position yet it creates a linknode where the value is the current value and the rest is recursively calling itself with the rest of the sequence and index - 1
        return lc.LinkNode(dna_seq1.value,substitution(dna_seq1.rest,idx-1,base))

def insertion(dna_seq1, dna_seq2, idx):
    """insertion inserts the second dna sequence in the first dna sequence at the indicated index and returns the new dna sequence
        dna_seq1: the sequence that is getting another sequence inserted into (a linknode)
        dna_seq2: the sequence being inserted (a linknode)
        idx: the index at which dna_seq2 is being inserted into dna_seq1
    """
    if idx == 0:
        #When the function reaches the intended index, the function concatenates the inserted sequence and the rest of the original sequence and returns it
        return lc.concatenate(dna_seq2, dna_seq1)
    elif dna_seq1 is None:
        #If it reaches the end of the sequence then an out of Index error is raised
        raise IndexError("Invalid Substitution Index")
    else:
        #If the program hasn't reached the index position yet it creates a linknode where the value is the current value of the first sequence and the rest is recursively calling itself with the rest of the first sequence and index - 1
        return lc.LinkNode(dna_seq1.value,insertion(dna_seq1.rest,dna_seq2,idx-1))

def deletion(dna_seq,idx,segment_size):
    """deletion deletes a certain part of the the dna sequence and returns the new dna sequence
        dna_seq: is the sequence that is going to get partially deleted (a linknode)
        idx: the index at which the deletion starts
        segment_size: the length of how many dna basses getting deleted
    """
    if idx == 0:
        #When the sequence reaches the index
        if segment_size == 0:
            #When the segment_size = 0 and the deleted portion is done being deleted, the function just returns the dna_seq
            return dna_seq
        elif dna_seq is None:
            #If it reaches the end of the sequence and idx = 0 then an out of Index error is raised
            raise IndexError("Invalid Deletion Index")
        else:
            #Deletes the current value by recursively calling itself with the rest of the dna sequence and segment size - 1
            return deletion(dna_seq.rest,idx,segment_size - 1)
    elif dna_seq is None:
        #If idx > 0 and the sequence finishes the program returns none
        return None
    else:
        #If the program hasn't reached the index position yet it creates a linknode where the value is the current value of the sequence and the rest is recursively calling itself with the rest of the sequence and index - 1
        return lc.LinkNode(dna_seq.value,deletion(dna_seq.rest,idx-1,segment_size))

def duplication(dna_seq,idx,segment_size):
    """duplication duplicates a part of a dna sequence and then returns the new linknode
        dna_seq: the dna sequence in which a part is being duplicated (a linknode)
        idx: the index at which the duplication starts
        segment_size: the length of the duplication sequence
        dup_seq: the reverse of the duplicated sequence (a linknode)
    """
    if idx == 0:
        #When the sequence reaches the index
        dup_seq = None
        if segment_size == 0:
            #If the segment_size = 0 then it returns the dna_seq
            return dna_seq
        while segment_size > 0:
            #While the segmented section of the sequence is getting duplicated (segment size >0)
            if dna_seq is None:
                #If it reaches the end of the sequence and idx = 0 then an out of Index error is raised
                raise IndexError("Invalid Duplication Index")
            else:
                #If the dna_seq isn't None then the duplicated sequence gets increased by the value in the dna_seq, then the dna sequence is equal to the rest and the segment_size gets smaller by one
                dup_seq = lc.LinkNode(dna_seq.value,dup_seq)
                dna_seq = dna_seq.rest
                segment_size += -1
        return lc.concatenate(lc.concatenate(lc.reverse_tail_rec(dup_seq),lc.reverse_tail_rec(dup_seq)),dna_seq)
                #Returns the the concatenation of the two reversed duplication sequences and the rest of the dna sequence
    elif dna_seq == None:
        #If idx > 0 and the sequence finishes the function returns none
        return None
    else:
        #If the program hasn't reached the index position yet it creates a linknode where the value is the current value of the sequence and the rest is recursively calling itself with the rest of the sequence and index - 1
        return lc.LinkNode(dna_seq.value,duplication(dna_seq.rest,idx-1,segment_size))