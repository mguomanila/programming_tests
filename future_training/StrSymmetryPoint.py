'''
StrSymmetryPoint
Find a symmetry point of a string, if any.

Write a function:

def solution(S):

that, given a string S, returns the index (counting from 0) of a character such that the part of the string to the left of that character is a reversal of the part of the string to its right. The function should return −1 if no such index exists.

Note: reversing an empty string (i.e. a string whose length is zero) gives an empty string.

For example, given a string:

"racecar"

the function should return 3, because the substring to the left of the character "e" at index 3 is "rac", and the one to the right is "car".

Given a string:

"x"

the function should return 0, because both substrings are empty.

Write an efficient algorithm for the following assumptions:

the length of S is within the range [0..2,000,000].
'''
from timeit import timeit
from string import ascii_letters as as_let
from random import randrange as r

def is_pal(str1,str2):
    if str1 == str2[::-1]:
        return True
    return False

def soln1(S):
    n = len(S)
    if n < 3: return 0
    for i in range(2,n//2+1):
        if i > 2:
            str1 = S[:i]
            str2 = S[i+1:i+i+1]
            if str1 == str2[::-1]:
                return i
    else:
        return 0

if __name__ == '__main__':
    s_min = 0
    s_max = 2*10*6
    ascii = as_let[:26]
    S = ''.join([ascii[r(0,26)] for i in range(s_max)])
    a = timeit('soln1(S)',number=1,globals=locals())
    S = 'racecar'
    soln1(S)
