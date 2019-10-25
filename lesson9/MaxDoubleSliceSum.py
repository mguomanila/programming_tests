'''
A non-empty array A consisting of N integers is given.

A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double slice.

The sum of double slice (X, Y, Z) is the total of A[X + 1] + A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].

For example, array A such that:

    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2
contains the following example double slices:

double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
double slice (3, 4, 5), sum is 0.
The goal is to find the maximal sum of any double slice.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the maximal sum of any double slice.

For example, given:

    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2
the function should return 17, because no double slice of array A has a sum of greater than 17.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [3..100,000];
each element of array A is an integer within the range [−10,000..10,000].
'''
from timeit import timeit
from random import randint as r

# score 
def soln1(A):
    n = len(A)
    if n <= 3:
        return 0
    sum_add = []
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                a = sum(A[i+1:j])
                b = sum(A[j+1:k])
                sum_add.append(a+b)
    return max(sum_add)

def soln2(A):
    n = len(A)
    if n <= 3:
        return 0
    sum_add = []

    
if __name__ == '__main__':
    n_min = 3
    n_max = 10**5
    a_min = -10**4
    a_max = 10**5
    A = [r(a_min,a_max) for i in range(n_max)]
    a = timeit('soln1(A)',number=10**0,globals=locals())
    soln1([3,2,6,-1,4,5,-1,2])
