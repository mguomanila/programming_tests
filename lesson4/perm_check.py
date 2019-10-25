'''
[75%] PermCheck
START
Check whether array A is a permutation.
Programming language:  
A non-empty array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
is a permutation, but array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

def solution(A)

that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
the function should return 1.

Given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
the function should return 0.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [1..1,000,000,000].
'''
from random import randrange as r, seed as s
import time


def soln1(A):
    N = len(A)
    upper_limit = 100000
    elem_lower = 1
    elem_upper = int(1e9)
    if not N or N > upper_limit: raise AssertionError
    for num in A:
        if num < elem_lower or num > elem_upper: raise AssertionError
    A = list(set(A))
    len_a = len(A)
    pos = 0
    if N == len_a:
        for i in range(1,len_a):
            if A[i-1] == (A[i] - 1): continue
            else:
                return 0
        else:
            return 1
    else:
        return 0


def soln2(A):
    # write your code in Python 3.6
    N = len(A)
    n_min = 1
    n_max = 10**5
    if N < n_min or N > n_max: raise AssertionError
    v_min = min(A)
    v_max = max(A)
    if v_min != 1: return 0
    if (v_max-v_min+1) % N != 0: return 0
    return 1


def soln3(A):
    start = time.clock()
    N = len(A)
    A = set(A)
    len_a = len(A)
    duplicate = True if len_a < N else False
    if duplicate: return 0
    lower = 1
    upper = int(1e5)
    elem = int(1e9)
    if N < lower or N > upper: raise AssertionError
    for num in A:
        if not isinstance(num, int): raise AssertionError
        if num < lower or num > elem: raise AssertionError
    counted = False
    key = 0
    is_perm = 0
    for num in A:
        if not counted:
            if num is not 1: break
            counted = True
        else:
            if num == (key+1): pass
            else: break
        key = num
    else:
        is_perm = 1
    print('time: %fs' %(time.clock()-start))
    return is_perm
