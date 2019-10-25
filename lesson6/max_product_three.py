'''
Task
A non-empty array A consisting of N integers is given. The product of triplet (P, Q, R) equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).

For example, array A such that:

  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6
contains the following example triplets:

(0, 1, 2), product is −3 * 1 * 2 = −6
(1, 2, 4), product is 1 * 2 * 5 = 10
(2, 4, 5), product is 2 * 5 * 6 = 60
Your goal is to find the maximal product of any triplet.

Write a function:

def solution(A)

that, given a non-empty array A, returns the value of the maximal product of any triplet.

For example, given array A such that:

  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6
the function should return 60, as the product of triplet (2, 4, 5) is maximal.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [3..100,000];
each element of array A is an integer within the range [−1,000..1,000].
'''
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from timeit import timeit
from random import randrange as r


def soln1(A):
    # write your code in Python 3.6
    count, triplet = 0, 1
    for num in sorted(A,reverse=1):
        if count < 3 and num > 0:
            triplet *= num
        elif count < 3 and num <= 0:
            if triplet > 1: break
            triplet *= num
        else: break
        count += 1
    return triplet

def soln2(A): # wrong!
    ar = sorted(A,reverse=1)
    ar = ar[:3] + ar[-3:]
    triplet,tm = 1, []
    for i in range(len(ar)-3):
        for j in range(i,i+3):
            triplet *= ar[j]
        #print(triplet)
        tm += [triplet]
        triplet = 1
    return max(tm)


def comb(x,r):
    from math import factorial as f
    return f(x)//(f(r)*f(x-r))


def counter(i,j,n):
    b = i+j
    b += 1
    c = b+1
    if not b < n:
        b = b - n
    if not c < n:
        c = c - n
    return b,c 


def soln3(A):
    A = sorted(A,reverse=1)
    n = len(A)
    triplet = []
    def trip(i,count,n):
        j,k = counter(i,count,n)
        return [A[i]*A[j]*A[k]]
    if n == 3:
        triplet = 1
        for i in range(n):
            triplet *= A[i]
        triplet = [triplet]
    elif n == 4:
        for i in range(2):
            for count in range(2):
                triplet += trip(i,count,n)
                #print(i,j,k,A[i]*A[j]*A[k])
    elif n == 5:
        for i in range(n):
            for count in range(3):
                triplet += trip(i,count,n)
                #print(i,j,k,A[i]*A[j]*A[k])
    else:
        A = A[:3] + A[-3:]
        n,nn = 6, 4
        for i in range(n):
            for count in range(nn):
                triplet += trip(i,count,n)
                #print(i,j,k,A[i]*A[j]*A[k])
    #print(len(triplet))
    return max(triplet)
    
    

if __name__ == '__main__':
    n_min = 3
    n_max = 10**5
    val_min = -10**3
    val_max = 10**3
    A = [r(val_min,val_max) for a in range(n_max)]
    #a = timeit('soln1(A)',number=10**0,globals=globals())
    b = timeit('soln3(A)',number=10**0,globals=globals())
    soln3([-3,1,2,-2,5,6])
    soln3([-1,-1,-1])
    soln3([-1000,-999,1000])
