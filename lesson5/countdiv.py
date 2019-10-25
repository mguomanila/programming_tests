'''
Task
Write a function:

def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.
'''
from timeit import timeit
from random import randrange as r
from array import array


def soln1(A, B, K):
    # write your code in Python 3.6
    count = 0
    for i in range(A,B+1):
        if i % K == 0:
            count += 1
    return count

def soln2(A,B,K):
    ar = array('L',(a for a in range(A,B+1)))
    for count

if __name__ == '__main__':
    n_min = 0
    n_max = 2*10**9
    v_min = 1
    A = r(n_min,(n_max/2)-1)
    B = r(n_max/2,n_max)
    K = r(A,B)
    #a = timeit('soln1(A, B, K)',number=10**1,globals=globals())
    #print(a)
    b = timeit('soln2(A, B, K)',number=10**1,globals=globals())
