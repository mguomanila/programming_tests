 '''
An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if it is possible to build a triangle with sides of lengths A[P], A[Q] and A[R]. In other words, triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

A[P] + A[Q] > A[R],
A[Q] + A[R] > A[P],
A[R] + A[P] > A[Q].
For example, consider array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 12
There are four triangular triplets that can be constructed from elements of this array, namely (0, 2, 4), (0, 2, 5), (0, 4, 5), and (2, 4, 5).

Write a function:

def solution(A)

that, given an array A consisting of N integers, returns the number of triangular triplets in this array.

For example, given array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 12
the function should return 4, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..1,000];
each element of array A is an integer within the range [1..1,000,000,000].

 '''
from timeit import timeit


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def is_triplet(q,p,r):
    triplet = False
    if 0 <= p < q < r < n:
        triplet = True
    if p + q > r:
        triplet = True
    if q + r > p:
        triplet = True
    if r + p > q:
        triplet = True
    return triplet

def combinations(n,r):
    if r > n: return
    indices = list(range(r))
    yield tuple(i for i in indices)
    while True:
        for i in reversed(indices):
            if indices[i] + r != i + n:
                indices[i] += 1
                for j in range(i+1, r):
                    indices[j] = indices[j-1] + 1
                yield tuple(i for i in indices)        
                break
        else:
            return

def soln1(A):
    # write your code in Python 3.6
    
    
    
if __name__ == '__main__':
    n_min = 0
    n_max = 10**3
    a_min = 1
    a_max = 10**9
    
