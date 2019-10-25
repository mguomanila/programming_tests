 '''
You have to climb up a ladder. The ladder has exactly N rungs, numbered from 1 to N. With each step, you can ascend by one or two rungs. More precisely:

        with your first step you can stand on rung 1 or 2,
        if you are on rung K, you can move to rungs K + 1 or K + 2,
        finally you have to stand on rung N.

Your task is to count the number of different ways of climbing to the top of the ladder.

For example, given N = 4, you have five different ways of climbing, ascending by:

        1, 1, 1 and 1 rung,
        1, 1 and 2 rungs,
        1, 2 and 1 rung,
        2, 1 and 1 rungs, and
        2 and 2 rungs.

Given N = 5, you have eight different ways of climbing, ascending by:

        1, 1, 1, 1 and 1 rung,
        1, 1, 1 and 2 rungs,
        1, 1, 2 and 1 rung,
        1, 2, 1 and 1 rung,
        1, 2 and 2 rungs,
        2, 1, 1 and 1 rungs,
        2, 1 and 2 rungs, and
        2, 2 and 1 rung.

The number of different ways can be very large, so it is sufficient to return the result modulo 2P, for a given integer P.

Write a function:

    def solution(A, B)

that, given two non-empty arrays A and B of L integers, returns an array consisting of L integers specifying the consecutive answers; position I should contain the number of different ways of climbing the ladder with A[I] rungs modulo 2B[I].

For example, given L = 5 and:
    A[0] = 4   B[0] = 3
    A[1] = 4   B[1] = 2
    A[2] = 5   B[2] = 4
    A[3] = 5   B[3] = 3
    A[4] = 1   B[4] = 1

the function should return the sequence [5, 1, 8, 0, 1], as explained above.

Write an efficient algorithm for the following assumptions:

        L is an integer within the range [1..50,000];
        each element of array A is an integer within the range [1..L];
        each element of array B is an integer within the range [1..30].
'''
from timeit import timeit
from random import randrange as r
from math import sqrt, pow
from array import array

def fib1(n):
    c = sqrt(5)
    a = (1 + c)/2
    b = (1 - c)/2
    d = pow(a,n)
    e = pow(b,n)
    return (d-e)/c

def fib2(n):
    a = [0,1]
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1        
    for i in range(1,n):
        a += [a[-1]+a[-2]]
    return a[-1]

def soln1(A, B):
    # write your code in Python 3.6
    pass
    n = len(A)
    if n != len(B): raise AssertionError
    return [int(fib1(A[i]+1) % pow(2,B[i])) for i in range(n)]

def soln2(A,B):
    n = len(A)
    return [fib2(A[i]+1) % int(pow(2,B[i])) for i in range(n)]

def soln3(A,B):
    

if __name__ == '__main__':
    a = soln2([4,4,5,5,1],[3,2,4,3,1])
    a_min = 1
    a_max = 5*10**3
    b_max = 30
    A = [r(1,a_max) for i in range(a_max)]
    B = [r(1,30) for i in range(len(A))]
    c = timeit('soln2(A, B)',number=1,globals=globals())
