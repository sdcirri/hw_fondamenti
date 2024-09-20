# -*- coding: utf-8 -*-
'''
    We have a sequence of N integers, with N odd.
    We apply the following procedure to the sequence, that could delete some elements from the sequence.
    - While there exists at least 2 equal numbers in the sequence:
        - we delete 2 of these equal numbers and keep the others in the same order.

    Given a n integer sequence as such, we want to find all final sequences obtained by repeatedly applying
    the above procedure until it's no more possible to do it.
    notice that all these sequences contain the same positive number of different integers.

    E.g. consider the three of sequences that we obtain from the sequence 1 2 0 1 0 0 1 
    by applying the procedure. You can see the tree in the file game_tree.pdf 
    The tree leaves are the final sequences.

    This is an example of a game tree implicitly defined by the game rules.
    - the root is the initial sequence
    - the daughter nodes of any node are obtained by deleting one pair of equal values
    - the leaves are the sequences where the procedure cannot be applied further

    You should define the ex1(sequence) recursive function 
    (or using other recursive functions or methods as you see fit) that:
    - receives as argument a string encoding the sequence of N integers with N odd
    (in the string all numbers are separated by a space)
    - returns a set containing the encodings (strings with integers separated by space)
      of all final sequences that it's possible to produce

    E.g. from the sequence '1 2 0 1 0 0 1' ex1 should return the set
      {'2 0 1', '2 1 0', '1 2 0'}

NOTICE: the timeout for this exercise is 1 second for each test
NOTICE: at heast one of the functions/methods used in the solution SHOULD be recursive
NOTICE: the test machinery automatically recognizes recursione ONLY for functions that are
        defined at the external level (no inner functions) or for methods
        DO NOT define the recursive functions inside another function/method
NOTICE: do not import other libraries or open other files

'''

def ex1(s):
    # put here your code
    pass











if __name__ == '__main__':
    pass
    # put here your personal tests

