'''
[0%] NumberOfDiscIntersections
START
Compute the number of intersections in a sequence of discs.
Programming language:  
We draw N discs on a plane. The discs are numbered from 0 to N − 1. An array A of N non-negative integers, specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].

We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point (assuming that the discs contain their borders).

The figure below shows discs drawn for N = 6 and A as follows:

  A[0] = 1
  A[1] = 5
  A[2] = 2
  A[3] = 1
  A[4] = 4
  A[5] = 0


There are eleven (unordered) pairs of discs that intersect, namely:

discs 1 and 4 intersect, and both intersect with all the other discs;
disc 2 also intersects with discs 0 and 3.
Write a function:

def solution(A)

that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

Given array A shown above, the function should return 11, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [0..2,147,483,647].

'''
from timeit import timeit
from random import randrange as r
from array import array


def soln1(A):
    n = len(A)
    catch = 0
    for i in range(n-1):
        f = (i-A[i],i+A[i])
        for j in range(i+1,n):
            l = (j-A[j],j+A[j])
            if (f[0] <= l[0] and f[1] >= l[0]) or (l[0] <= f[1] and l[1] >= f[1]):
                catch += 1
    if catch > 10**7: return -1
    return catch

def soln2(A):
    A = array('L', (a for a in A))
    n = len(A)
    catch = 0
    for i in range(n-1):
        f = (i-A[i],i+A[i])
        for j in range(i+1,n):
            l = (j-A[j],j+A[j])
            if (f[0] <= l[0] and f[1] >= l[0]) or (l[0] <= f[1] and l[1] >= f[1]):
                catch += 1
    if catch > 10**7: return -1
    return catch


if __name__ == '__main__':
    #soln1([1,5,2,1,4,0])
    n_min = 0
    n_max = 10**4
    val_max = 2147483647
    val_max2 = 483647
    A = array('L',(r(n_min,val_max2) for a in range(n_max)))
    a = timeit('soln1(A)',number=1,globals=globals())
    # 14.2 s ± 147 ms per loop (mean ± std. dev. of 7 runs, 1 loop each) not fast!
    #b = timeit('soln2(A)',number=1,globals=globals())
