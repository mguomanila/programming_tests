'''
Peaks
Divide an array into the maximum number of same-sized blocks, each of which should contain an index P such that A[P - 1] < A[P] > A[P + 1].


A non-empty array A consisting of N integers is given.

A peak is an array element which is larger than its neighbors. More precisely, it is an index P such that 0 < P < N − 1,  A[P − 1] < A[P] and A[P] > A[P + 1].

For example, the following array A:

    A[0] = 1
    A[1] = 2
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2
has exactly three peaks: 3, 5, 10.

We want to divide this array into blocks containing the same number of elements. More precisely, we want to choose a number K that will yield the following blocks:

A[0], A[1], ..., A[K − 1],
A[K], A[K + 1], ..., A[2K − 1],
...
A[N − K], A[N − K + 1], ..., A[N − 1].
What's more, every block should contain at least one peak. Notice that extreme elements of the blocks (for example A[K − 1] or A[K]) can also be peaks, but only if they have both neighbors (including one in an adjacent blocks).

The goal is to find the maximum number of blocks into which the array A can be divided.

Array A can be divided into blocks as follows:

one block (1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2). This block contains three peaks.
two blocks (1, 2, 3, 4, 3, 4) and (1, 2, 3, 4, 6, 2). Every block has a peak.
three blocks (1, 2, 3, 4), (3, 4, 1, 2), (3, 4, 6, 2). Every block has a peak. Notice in particular that the first block (1, 2, 3, 4) has a peak at A[3], because A[2] < A[3] > A[4], even though A[4] is in the adjacent block.
However, array A cannot be divided into four blocks, (1, 2, 3), (4, 3, 4), (1, 2, 3) and (4, 6, 2), because the (1, 2, 3) blocks do not contain a peak. Notice in particular that the (4, 3, 4) block contains two peaks: A[3] and A[5].

The maximum number of blocks that array A can be divided into is three.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the maximum number of blocks into which A can be divided.

If A cannot be divided into some number of blocks, the function should return 0.

For example, given:

    A[0] = 1
    A[1] = 2
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2
the function should return 3, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [0..1,000,000,000].

''' 
'''
he following issues have been detected: wrong answers.

For example, for the input [1, 2, 3, 4, 5, 6] the solution returned a wrong answer (got 1 expected 0).

prime_length 
test with prime sequence length ✘WRONG ANSWER 
got 5 expected 1
1. 0.036 s OK
2. 0.036 s OK
3. 0.036 s WRONG ANSWER,  got 5 expected 1


medium_random 
chaotic medium sequences, length = ~5,000 ✘WRONG ANSWER 
got 1692 expected 625
1. 0.044 s WRONG ANSWER,  got 1692 expected 625
2. 0.044 s WRONG ANSWER,  got 626 expected 100

medium_anti_slow 
medium test anti slow solutions ✘WRONG ANSWER 
got 2310 expected 1
1. 0.048 s WRONG ANSWER,  got 2310 expected 1

large_random 
chaotic large sequences, length = ~50,000 ✘WRONG ANSWER 
got 16648 expected 5000
1. 0.104 s WRONG ANSWER,  got 16648 expected 5000
2. 0.100 s WRONG ANSWER,  got 9290 expected 1250

large_anti_slow 
large test anti slow solutions ✘WRONG ANSWER 
got 45044 expected 30030
1. 0.144 s OK
2. 0.156 s WRONG ANSWER,  got 45044 expected 30030

extreme_max 
extreme max test ✘WRONG ANSWER 
got 49999 expected 25000
1. 0.172 s WRONG ANSWER,  got 49999 expected 25000
2. 0.160 s OK


'''
from timeit import timeit
from random import randint as r


def soln1(A):
    n = len(A)
    if n <= 2:
        return 0
    peak = []
    for i in range(n):
        if i == 0:
            if A[i+1] < A[i] > A[i+2]:
                peak.append(A[i])
        if i >= 1 and i < n-1:
            if A[i-1] < A[i] > A[i+1]:
                peak.append(A[i])
        if i == n-1:
            if A[i-1] < A[i] > A[i-2]:
                peak.append(A[i])
    return len(peak)
    
    
if __name__ == '__main__':
    n_min = 1
    n_max = 10**5
    a_min = 0
    a_max = 10**9
    A = [r(a_min,a_max) for i in range(n_max)]
    a = timeit('soln1(A)',number=10**0,globals=locals())
    soln1([1,2,3,4,3,4,1,2,3,4,6,2])
