# -*- coding: utf-8 -*-
'''
In poetry, as well as in music, there exist the notion of rhythm.
In music, rhythm is that characteristic of the song you're listening to that makes you
tap your foot or hands in time, or guides you while you are dancing.
Similarly, poems (except those written in free verse) also have a rhythm, determined
by the accents on the syllables that make up their verses.
Some poems  have a rhythm that is the same in each line of text, while others have a rhythm
that changes slightly between one line and the next.
We would like to try to estimate how much regular (i.e., in sync)
or irregular (i.e., out of sync) a poem is in terms of the rhythm
contained in its verses. The more the lines of the poem all have the same rhythm,
the higher the regularity (and then the sync) of the poem, and vice-versa.

Every word in any language is composed of syllables which are pronounced using the intonation of the
voice to give them a stronger or weaker accent. For example, in Italian the word "casa" has an accent
on the first syllable. There is a way to specify this; it is called the phonetic transcription
of a word: in the example, the phonetic transcription of "casa" is "kˈaza", where the apostrophe
indicates that there is a primary accent on the first syllable (ka).

We want to write a program that, given a text file with encoding 'utf-8'
containing the lines of a poem (there can also be blank lines, which we will ignore),
finds the accents of each word and then of the whole poem, while maintaining the subdivision
of the poem in lines, as in the original text.
To do this, we will use two functions, "phones_for_word" and "stresses", of the "pronouncing" module
(https://pronouncing.readthedocs.io/en/latest/).
Given a non-empty line of the poem, we will call the function phones_for_word on each word,
obtaining its phonetic translation (casa -> k'asa).
The function might return more than one phonetic translation for the same word, in
case that word can be pronounced in different ways, in that case we will consider
only its first phonetic translation.
At that point, we will call the function stresses, that, given as input the phonetic translation of the word,
will return a string of accents, in which: 0=no accent, 1=primary accent,
2=secondary accent. For our purposes, we will consider only primary accents, then
we will leave out secondary accents, considering them the same as no accents (i.e., as if they were zeros).
Also, when translating whole sentences into accents, we will add a zero between each pair of words
(see also Note 2 below).

Note 1: When translating words into phonemes, the phones_for_word function may return
an empty list (because the word is unknown); in that case we will consider as accents
a sequence of zeros equal to the length of the word divided by two (integer part of the result);
for example, since "pierc" has no phonetic translation, we consider as accents the string "00".

Note 2: to simplify, there will always be an extra zero after the last word of each line

For example, given the line of text: "IN the midway of this our mortal life,"
we will obtain the list of accents: [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0]
In fact:
IN -> ['IH0 N', 'IH1 N'] -> 0
space -> 0
the -> ['DH AH0', 'DH AH1', 'DH IY0'] -> 0
space -> 0
midaway - > ['M IH1 D W EY2'] -> 1,0
space -> 0
of -> ['AH1 V'] -> 1
space -> 0
this -> ['DH IH1 S', 'DH IH0 S'] -> 1
space -> 0
our -> ['AW1 ER0', 'AW1 R', 'AA1 R'] -> 1,0
space -> 0
mortal -> ['M AO1 R T AH0 L'] -> 1,0
space -> 0
life -> ['L AY1 F'] -> 1
space -> 0

Once we have translated the entire poem into sequences of zeros and ones, we will have a list of lists
of various lengths, for example:

IN the midway of this our mortal life,
I found me in a gloomy wood, astray
Gone from the path direct: and e'en to tell
It were no easy task, how savage wild
That forest, how robust and rough its growth,
Which to remember only, my dismay
Renews, in bitterness not far from death.

[
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0]
]

We now want to transform this list of lists into a matrix of accents,
by adding an appropriate number of zeros at the end of the rows
that are shorter than the longest row:

[
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0]
]

We now calculate the synchronization between all possible pairs of rows
in the matrix. Given two lists A and B, each of N values 0 or 1, and a value tau
between zero and N, we define the synchronization index between A and B as:

       0.5 * (c(B|A) + c(A|B))
Sync = -----------------------
          sqrt(m(A)*m(B))

Where:
    - c(B|A) is the number of times an accent of B is preceded by an accent of A
      within a distance <= tau
    - c(A|B) is the number of times an accent of A is preceded by an accent of B
       within a distance <= tau
    - m(A) is the number of accents in A
    - m(B) is the number of accents in B

and where, remember, a value of 1 in A or B represents an accent

NOTA: if m(A) == 0 o m(B) == 0 then we assume zero Sync

For example, given the two sequences:
    - A = [0, 0, 0, 0, 1, 0, 0, 1]
    - B = [1, 0, 1, 0, 1, 0, 0, 0]
    - tau = 3

we will obtain:
    - c(B|A) = 1, as only the third accent in B (position 4) is preceded in A by a
    accent within 3 positions (in this case the 1 in A has the same position
    as the 1 in B)
    - c(A|B) = 2, as both accents of A are preceded in B by two accents within
    3 positions
    - m(A) = 2
    - m(B) = 3
    - Sync = 0.5 * (1 + 2) / sqrt(2 * 3) = 0.6123724356957946

Given an input poem, we define the poem sync as
the average of the Sync values computed on all pairs of lines (A1, A2)
where A1 and A2 are not the same line
NOTE: two different lines can still contain the same values!

Write a function PoemSync that, given in input:
- the path of a text file containing a poem
- the path to the output file for saving the matrix of accents
- the value (integer) of tau

performs the following operations
- opens the poem file and calculates the matrix of accents
- saves the accents matrix in the file whose path is provided as input
- calculates and returns the synchronization of the poem, rounded off
  to the sixth decimal place (e.g.: 0.6123724356957946 -> 0.612372)

note: going back to the accents matrix mentioned above, the file generated by
by PoemSync will contain:

000010010101001001000
101010000010010010000
101000100100010101010
101010100101010010000
101001001000101010000
101001001001001000000
010001000101010100000


EXAMPLE OF EXECUTION:

PoemSync("example.txt", "example.out.txt", 2)

example.txt:
No one can tell me
Where the wind comes from
Where the wind comes from

no one can tell me
['no', 'one', 'can', 'tell', 'me']
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
where the wind comes from
['where', 'the', 'wind', 'comes', 'from']
[1, 0, 0, 0, 1, 0, 1, 0, 1, 0]
where the wind comes from
['where', 'the', 'wind', 'comes', 'from']
[1, 0, 0, 0, 1, 0, 1, 0, 1, 0]

matrix:
1010101010
1000101010
1000101010

sync between a=[1, 0, 1, 0, 1, 0, 1, 0, 1, 0] and
             b=[1, 0, 0, 0, 1, 0, 1, 0, 1, 0]
(c(b|a), m(b)) = (4, 4) (c(a|b), m(a)) = (5, 5)
sync = 1.0062305898749053

sync between a=[1, 0, 1, 0, 1, 0, 1, 0, 1, 0] and
             b=[1, 0, 0, 0, 1, 0, 1, 0, 1, 0]
(c(b|a), m(b)) = (4, 4) (c(a|b), m(a)) = (5, 5)
sync = 1.0062305898749053

sync between a=[1, 0, 0, 0, 1, 0, 1, 0, 1, 0] and
             b=[1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
(c(b|a), m(b)) = (5, 5) (c(a|b), m(a)) = (4, 4)
sync = 1.0062305898749053

sync between a=[1, 0, 0, 0, 1, 0, 1, 0, 1, 0] and
             b=[1, 0, 0, 0, 1, 0, 1, 0, 1, 0]
(c(b|a), m(b)) = (4, 4) (c(a|b), m(a)) = (4, 4)
sync = 1.0

sync between a=[1, 0, 0, 0, 1, 0, 1, 0, 1, 0] and
             b=[1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
(c(b|a), m(b)) = (5, 5) (c(a|b), m(a)) = (4, 4)
sync = 1.0062305898749053

sync between a=[1, 0, 0, 0, 1, 0, 1, 0, 1, 0] and
             b=[1, 0, 0, 0, 1, 0, 1, 0, 1, 0]
(c(b|a), m(b)) = (4, 4) (c(a|b), m(a)) = (4, 4)
sync = 1.0

PoemSync = 1.004154

TIMEOUT: 0.5s

'''

import pronouncing
import math

def PoemSync(inputfilename, outputfilename, tau):
    # your code goes here
    pass

if __name__ == "__main__":
    # your tests go here
    pass
