'''
A non-empty array A consisting of N numbers is given. The array is sorted in non-decreasing order. The absolute distinct count of this array is the number of distinct absolute values among the elements of the array.

For example, consider array A such that:

  A[0] = -5
  A[1] = -3
  A[2] = -1
  A[3] =  0
  A[4] =  3
  A[5] =  6
The absolute distinct count of this array is 5, because there are 5 distinct absolute values among the elements of this array, namely 0, 1, 3, 5 and 6.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N numbers, returns absolute distinct count of array A.

For example, given array A such that:

  A[0] = -5
  A[1] = -3
  A[2] = -1
  A[3] =  0
  A[4] =  3
  A[5] =  6
the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647];
array A is sorted in non-decreasing order.
'''
from timeit import timeit
from random import randint as r


def soln1(A):
    # write your code in Python 3.6
    n = len(A)
    A = set([abs(A[i]) for i in range(n)])
    return len(A)


if __name__ == '__main__':
    n_min = 1
    n_max = 10**5
    val_min = -2147483647
    val_max = 2147483647
    A = [r(val_min,val_max) for i in range(n_max)]
    a = soln1([1,2,-1])
    b = timeit('soln1(A)',number=1,globals=globals())
    print(b)
