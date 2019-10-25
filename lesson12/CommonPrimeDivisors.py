'''
RESPECTABLE
CommonPrimeDivisors
Check whether two numbers have the same prime divisors.

A prime is a positive integer X that has exactly two distinct divisors: 1 and X. The first few prime integers are 2, 3, 5, 7, 11 and 13.

A prime D is called a prime divisor of a positive integer P if there exists a positive integer K such that D * K = P. For example, 2 and 5 are prime divisors of 20.

You are given two positive integers N and M. The goal is to check whether the sets of prime divisors of integers N and M are exactly the same.

For example, given:

N = 15 and M = 75, the prime divisors are the same: {3, 5};
N = 10 and M = 30, the prime divisors aren't the same: {2, 5} is not equal to {2, 3, 5};
N = 9 and M = 5, the prime divisors aren't the same: {3} is not equal to {5}.
Write a function:

def solution(A, B)

that, given two non-empty arrays A and B of Z integers, returns the number of positions K for which the prime divisors of A[K] and B[K] are exactly the same.

For example, given:

    A[0] = 15   B[0] = 75
    A[1] = 10   B[1] = 30
    A[2] = 3    B[2] = 5
the function should return 1, because only one pair (15, 75) has the same set of prime divisors.

Write an efficient algorithm for the following assumptions:

Z is an integer within the range [1..6,000];
each element of arrays A, B is an integer within the range [1..2,147,483,647].
''' 
from timeit import timeit
from random import randrange as r
from math import sqrt, ceil

def divisors(N):
    divs = set()
    for i in range(2,int(sqrt(N))):
        a,b = divmod(N,i)
        if not b:
            divs.add(a)
            divs.add(i)
    return divs

def soln1n(A, B):
    # write your code in Python 3.6
    n = len(A)
    count = 0
    for i in range(n):
        a = divisors(A[i])
        b = divisors(B[i])
        #print(a,b)
        if a == b: count += 1
    return count

def gcd(n):
    gcd = []
    for i in range(2,ceil(sqrt(n))+2):
        a,b = divmod(n,i)
        if not b:
            gcd.append(i)
    return gcd

# Correctness: 28%
def soln2(A,B):
    # write your code in Python 3.6
    n = len(A)
    pairs = 0
    for i in range(n):
        a = set(gcd(A[i]))
        b = set(gcd(B[i]))
        if not a:
            a = set([A[i]])
        if not b:
            b = set([B[i]])
        if a == b:
            pairs += 1
    return pairs
        
        
if __name__ == '__main__':
    z_min = 1
    z_max = 6*10**3
    a_max = 2147483647
    n = r(z_min,z_max)
    A = [r(z_min,a_max) for i in range(z_max)]
    B = [r(z_min,a_max) for i in range(z_max)]
    a = timeit('soln2(A,B)',number=0,globals=locals())
    A = [7, 17, 5, 3]
    B = [7, 11, 5, 2]
    b = soln2(A,B)
    A = [6059, 551] 
    B = [442307, 303601]
    c = soln2(A,B)
