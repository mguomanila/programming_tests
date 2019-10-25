'''
[66%] OddOccurrencesInArray
START
Find value that occurs in odd number of elements.
Programming language:  Spoken language:  
A non-empty array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.

For example, in array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the elements at indexes 0 and 2 have value 9,
the elements at indexes 1 and 3 have value 3,
the elements at indexes 4 and 6 have value 9,
the element at index 5 has value 7 and is unpaired.
Write a function:

class Solution { public int solution(int[] A); }

that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.

For example, given array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the function should return 7, as explained in the example above.

Write an efficient algorithm for the following assumptions:

N is an odd integer within the range [1..1,000,000];
each element of array A is an integer within the range [1..1,000,000,000];
all but one of the values in A occur an even number of times.
'''
from timeit import timeit


def soln1(A):
    # write your code in Python 3.6
    N = len (A)
    min = 1
    max = 10**6
    if N < min or N > max: raise AssertionError
    val_min = 1
    val_max = 10**9
    valid = True
    B = set(A)
    count = 0
    odd = 0
    for val in B:
        if not isinstance(val,int): 
            valid=False
            break
        if val < val_min or val > val_max:
            valid=False
            break
        if A.count(val) % 2 != 0:
            count += 1
            odd = val
        if count > 1:
            valid=False
            break
    else:
        if count != 1:
            valid = False
    if not valid: raise AssertionError
    return odd


def soln2(A):
    # write your code in Python 3.6
    N = len (A)
    min = 1
    max = 10**6
    if N < min or N > max: raise AssertionError
    val_min = 1
    val_max = 10**9
    valid = True
    #B = set(A)


def soln3(A):
    pass


if __name__ == '__main__':
    a = timeit('',number=10,globals=globals())
