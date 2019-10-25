'''
CountNonDivisible
Calculate the number of elements of an array that are not divisors of each element.


You are given an array A consisting of N integers.

For each number A[i] such that 0 ≤ i < N, we want to count the number of elements of the array that are not the divisors of A[i]. We say that these elements are non-divisors.

For example, consider integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 3
    A[4] = 6
For the following elements:

A[0] = 3, the non-divisors are: 2, 6,
A[1] = 1, the non-divisors are: 3, 2, 3, 6,
A[2] = 2, the non-divisors are: 3, 3, 6,
A[3] = 3, the non-divisors are: 2, 6,
A[4] = 6, there aren't any non-divisors.
Write a function:

def solution(A)

that, given an array A consisting of N integers, returns a sequence of integers representing the amount of non-divisors.

Result array should be returned as an array of integers.

For example, given:

    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 3
    A[4] = 6
the function should return [2, 4, 3, 2, 0], as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..50,000];
each element of array A is an integer within the range [1..2 * N].
''' 
from timeit import timeit
from random import randint as r

def soln1(A):
    n = len(A)
    non_div = 0
    count_non_div = []
    for i in range(n):
        for j in range(n):
            if A[i] % A[j] != 0:
                non_div += 1
        count_non_div.append(non_div)
        non_div = 0
    return count_non_div

def soln2(A):
    n = len(A)
    A.sort(reverse=True)
    for i in range(int(sqrt(n))):
        


if __name__ == '__main__':
    n_min = 1
    n_max = 5*10**4
    a_min = 1
    a_max = 2*n_max
    A = [r(a_min,a_max) for i in range(n_max)]
    a = timeit('soln1(A)',number=10**0,globals=locals())
    soln1([3,1,2,3,6])
