'''
MaxSliceSum
Find a maximum sum of a compact subsequence of array elements.

A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A. The sum of a slice (P, Q) is the total of A[P] + A[P+1] + ... + A[Q].

Write a function:

def solution(A)

that, given an array A consisting of N integers, returns the maximum sum of any slice of A.

For example, given array A such that:

A[0] = 3  A[1] = 2  A[2] = -6
A[3] = 4  A[4] = 0
the function should return 5 because:

(3, 4) is a slice of A that has sum 4,
(2, 2) is a slice of A that has sum −6,
(0, 1) is a slice of A that has sum 5,
no other slice of A has sum greater than (0, 1).
Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..1,000,000];
each element of array A is an integer within the range [−1,000,000..1,000,000];
the result will be an integer within the range [−2,147,483,648..2,147,483,647].
'''
from timeit import timeit
from random import randint as r

# 46% score
def soln1(A):
    # write your code in Python 3.6
    n = len(A)
    if n==1:
        return A[0]
    sum_add = []
    for i in range(n-1):
        for j in range(i+1, n):
            sum_add.append(sum(A[i:j+1]))
    return max(sum_add)

def soln2(A):
    n = len(A)
    
    

if __name__ == '__main__':
    n_min = 1
    n_max = 10**6
    a_min = -2147483648
    a_max = 2147483648
    A = [r(a_min,a_max) for i in range(n_max)]
    a = timeit('soln1(A)',number=10**0,globals=locals())
    soln1([3,2,-6,4,0])
    soln1([-1,-2])
    
