'''
CountSemiprimes
Count the semiprime numbers in the given range [a..b]

A prime is a positive integer X that has exactly two distinct divisors: 1 and X. The first few prime integers are 2, 3, 5, 7, 11 and 13.

A semiprime is a natural number that is the product of two (not necessarily distinct) prime numbers. The first few semiprimes are 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

You are given two non-empty arrays P and Q, each consisting of M integers. These arrays represent queries about the number of semiprimes within specified ranges.

Query K requires you to find the number of semiprimes within the range (P[K], Q[K]), where 1 ≤ P[K] ≤ Q[K] ≤ N.

For example, consider an integer N = 26 and arrays P, Q such that:

    P[0] = 1    Q[0] = 26
    P[1] = 4    Q[1] = 10
    P[2] = 16   Q[2] = 20
The number of semiprimes within each of these ranges is as follows:

(1, 26) is 10,
(4, 10) is 4,
(16, 20) is 0.
Write a function:

def solution(N, P, Q)

that, given an integer N and two non-empty arrays P and Q consisting of M integers, returns an array consisting of M elements specifying the consecutive answers to all the queries.

For example, given an integer N = 26 and arrays P, Q such that:

    P[0] = 1    Q[0] = 26
    P[1] = 4    Q[1] = 10
    P[2] = 16   Q[2] = 20
the function should return the values [10, 4, 0], as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..50,000];
M is an integer within the range [1..30,000];
each element of arrays P, Q is an integer within the range [1..N]; P[i] ≤ Q[i].
'''
from timeit import timeit
from random import randrange as r


def sieve(n):
    sieve = [1] * (n+1)
    sieve[0] = sieve[1] = 0
    i = 2
    while i*i <= n:
        if sieve[i]:
            k = i*i
            while k <= n:
                sieve[k] = 0
                k += i
        i += 1
    return sieve

def array_factor(n):
    F = [0] * (n+1)
    i = 2
    while i*i <= n:
        if F[i] == 0: 
            k = i*i
            while k <= n:
                if F[k] == 0:
                    F[k] = i
                k += i
        i += 1
    return F

def factorization(x,F):
    prime_factors = []
    while F[x] > 0:
        prime_factors += [F[x]]
        _,x = divmod(x,F[x])
    prime_factors += [x]
    return prime_factors

def factorization2():
    

def semi_primes(n,x,y):
    primes = sieve(n)
    f = array_factor(n)
    a = set()
    print(primes)
    print(f)
    print(my_sieve4(n))
    for i in range(len(primes)):
        if primes[i] and i >= x and i <= y:
            b = factorization(i,f)
            print(x,y,i,b)
            for num in b:
                a.add(num)
    return len(a)

def my_sieve4(n):
    sievex = sieve(n)
    sievev = [a for a in range(n+1)]
    ar = []
    for i in range(len(sievex)):
        if sievex[i]:
            ar.append(sievev[i])
        else: ar.append(0)
    return ar

def soln1(N, P, Q):
    # write your code in Python 3.6
    m = len(P)
    mm = len(Q)
    if m != mm: raise AssertionError
    #m_min = 1
    #m_max = 3*10**4
    #if m != len(Q) or m < m_min or m > m_max: raise AssertionError
    #n_min = 1
    #n_max = 5*10**4
    #if N < n_min or N > n_max: raise AssertionError
    a = []
    for i in range(m):
        if P[i] > Q[i]: raise AssertionError
        a.append(semi_primes(N,P[i],Q[i]))
    return a

def soln2(N,P,Q):
    m = len(P)
    mm = len(Q)
    if m != mm: raise AssertionError
    for i in range(m):
        
    

if __name__ == '__main__':
    n_min = 1
    n_max = 5*10**4
    m_max = 3*10**4
    N = r(n_min,n_max)
    n_mid = N//2
    P = [r(n_min,n_mid) for a in range(N)]
    Q = [r(n_mid,N) for a in range(N)]
    a = timeit('soln2(N, P, Q)',number=10**0,globals=locals())
    b = soln2(26, [1, 4, 16], [26, 10, 20])
    
