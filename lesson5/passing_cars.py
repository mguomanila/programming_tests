'''
Task
A non-empty array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.

Array A contains only 0s and/or 1s:

0 represents a car traveling east,
1 represents a car traveling west.
The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.

For example, consider array A such that:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the number of pairs of passing cars.

The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.

For example, given:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer that can have one of the following values: 0, 1.
'''

from random import randrange as r
from timeit import timeit
from array import array


def soln1(A):
    N = len(A)
    upper = int(1e5)
    lower = 1
    exceed = int(1e9)
    if N < lower or N > upper: raise AssertionError
    for num in A:
        if not isinstance(num,int): raise AssertionError
        if num is not 0 and num is not 1: raise AssertionError
    count = 0
    for i in range(N):
        if A[i] is 0:
            for j in range(i+1, N):
                if A[j] is 1:
                    count += 1
        if count > exceed: count = -1
    #print('time: %fs'%(time.clock()-start))
    #print (A)
    return count


def soln2(A):
    N = len(A)
    upper = int(1e5)
    lower = 1
    exceed = int(1e9)
    if N < lower or N > upper: raise AssertionError
    for num in A:
        if not isinstance(num,int): raise AssertionError
        if num is not 0 and num is not 1: raise AssertionError
    def passing(q):
        return len([a for a in q if a is 1])
    count = 0
    for i in range(N):
        if A[i] == 0:
            count += passing(A[i+1:])
    #print('time: %fs'%(time.clock()-start))
    #print (A)
    return count

def soln3(A):
    passing, exceed = 0, 10**9
    n,count = len(A),0
    for i in range(n-1):
        for j in range(i+1,n):
            if A[i]==1:
                break
            if A[i]==0 and A[j]==1:
                count += 1
            if count > exceed: return -1
    return count

def soln4(A):
    n = len(A)
    def passing(q):
        return len([a for a in q if a is 1])
    count = 0
    for i in range(n):
        if A[i] == 0:
            count += passing(A[i+1:])
    return count


if __name__ == '__main__':
    n_min = 1
    n_max = 10**5
    elem = (0,2) 
    A = [r(elem[0],elem[1]) for a in range(n_max)]
    a = timeit('soln4(A)',number=10**0,globals=globals())
    #%timeit soln1(A)
    #%timeit soln2(A)
    #%timeit soln3(A)
    #%timeit soln4(A)
