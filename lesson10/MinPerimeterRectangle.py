'''
MinPerimeterRectangle
Find the minimal perimeter of any rectangle whose area equals N.

An integer N is given, representing the area of some rectangle.

The area of a rectangle whose sides are of length A and B is A * B, and the perimeter is 2 * (A + B).

The goal is to find the minimal perimeter of any rectangle whose area equals N. The sides of this rectangle should be only integers.

For example, given integer N = 30, rectangles of area 30 are:

(1, 30), with a perimeter of 62,
(2, 15), with a perimeter of 34,
(3, 10), with a perimeter of 26,
(5, 6), with a perimeter of 22.
Write a function:

def solution(n)

that, given an integer N, returns the minimal perimeter of any rectangle whose area is exactly equal to N.

For example, given an integer N = 30, the function should return 22, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..1,000,000,000].
''' 
from timeit import timeit
from random import randint as r
from math import sqrt

# score 90%
def soln1(N):
    # write your code in Python 3.6
    factor,per_list = [],[]
    for i in range(1,int(sqrt(N))+1):
        a,b = divmod(N,i)
        if b == 0:
            factor.append((a,i))
    for a,b in factor:
        P = 2 * (a+b)
        per_list.append(P)
    return min(per_list)


if __name__ == '__main__':
    n_min = 1
    n_max = 10**9
    N = r(n_min,n_max)
    a = timeit('soln1(N)',number=10**0,globals=locals())
    soln1(1)
