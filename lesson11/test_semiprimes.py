'''
Task description
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
each element of arrays P, Q is an integer within the range [1..N];
P[i] ≤ Q[i].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
'''
from timeit import timeit
from random import randrange as r
from bisect import insort


def sieve1(n):
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


def prime(n):
    sievex = sieve1(n)
    n += 1
    sievev = [a for a in range(n)]
    return [sievev[i] for i in range(n) if sievex[i]]


def semi_prime1(p,x,y):
    count, mult = [], []
    for n in p:
        mult += [n]
        for m in mult:
            t = m*n
            if t >= x and t <= y:
                count += [t]
            else:
                break
        if n*2 > y: break
    return sorted(count)

def semi_prime3(p,x,y):
    count, mult = [], []
    for n in p:
        mult.append(n)
        for m in mult:
            t = m*n
            if t >= x and t <= y:
                count.append(t)
            else:
                break
        if n*2 > y: break
    return sorted(count)

def semi_prime2(p,x,y):
    count, temp = [], []
    for n in p:
        temp.append(n)
        for m in temp:
            t = m*n
            if t >= x and t <= y:
                insort(count,t)
            else:
                break
        if n*2 > y: break
    return count


def solution(N, P, Q):
    # write your code in Python 3.6
    n_min = 1
    n_max = 5*10**4
    if N < n_min or N > n_max: raise AssertionError
    m_max = 3*10**4
    m = len(P)
    if m < n_min or m > m_max: raise AssertionError
    def valid(x):
        if x < n_min or x > n_max: return 0
        else: return 1
    primes = prime(N)
    count = []
    for i in range(m):
        #if not valid(P[i]) or not valid(Q[i]): raise AssertionError
        count += [len(semi_prime1(primes,P[i],Q[i]))]
    return count


if __name__ == '__main__':
    m_max = 3*10**4
    pi_min = 1
    pi_max = qi_min = 25*10**3
    qi_max = 5*10**4
    a = timeit('solution(26, [1, 4, 16], [26, 10, 20])',number=10**3,globals=globals())
    b1 = solution(r(1,10*2),[r(1,10**2) for a in range(10**3)],[r(10**2,10**3) for a in range(10**3)])
    b2 = semi_prime1(prime(300),1,110)
    n = r(1,5*10**4)
    p = [r(pi_min,pi_max) for a in range(m_max)]
    q = [r(qi_min,qi_max) for a in range(m_max)]
    c = timeit('solution(n,p,q)',number=10**1,globals=globals())
    # c1 = 258.6000018019986 sec  
    # c2 = 291.3942718920007
    # c3 = 165.77349500299897
    # c4 = 352.21955310901103
    #d1 = timeit('semi_prime1(prime(n),1,5*10**4)',number=10**3,globals=globals()) # 10.007284531006007 wins
    #d2 = timeit('semi_prime2(prime(n),1,5*10**4)',number=10**3,globals=globals()) # 30.273399308003718 loss
           
