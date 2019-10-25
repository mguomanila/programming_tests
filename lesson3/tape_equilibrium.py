'''
PAINLESS
[53%] TapeEquilibrium
START
Minimize the value |(A[0] + ... + A[P-1]) - (A[P] + ... + A[N-1])|.
Programming language:  
A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

For example, consider array A such that:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
We can split this tape in four places:

P = 1, difference = |3 − 10| = 7 
P = 2, difference = |4 − 9| = 5 
P = 3, difference = |6 − 7| = 1 
P = 4, difference = |10 − 3| = 7 
Write a function:

class Solution { public int solution(int[] A); }

that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

For example, given:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−1,000..1,000].
'''
from timeit import timeit


def soln1(A):
    start = time.clock()
    N = len(A)
    upper_limit = 100000
    if not N and N > upper_limit: raise AssertionError
    elem_lower = -1000
    elem_upper = 1000
    for num in A:
        if not isinstance(num,int): raise AssertionError
        if num < elem_lower or num > elem_upper: raise AssertionError
    P = {}
    count1 = 0
    for i in range(N-1):
        count1 += A[i]
        count2 = 0
        for j in range(i+1, N):
            count2 += A[j]
        P[i+1] = abs(count1-count2)
    count = 0
    for i in range(1,len(P)+1):
        if i == 1:
            count = P[i]
        else:
            if P[i] < count:
                count = P[i]
    else:
        print('time: %fs' % (time.clock()-start))
        return count


def soln3(A):
    # check integrity
    N = len(A)
    upper_limit = 100000
    if not N or N > upper_limit: raise AssertionError
    elem_lower = -1000
    elem_upper = 1000
    for num in A:
        if not isinstance(num,int) or num < elem_lower or num > elem_upper
    for i in range(N):
        

def soln3(A):
    # write your code in Python 3.6
    N = len(A)
    n_min = 2
    n_max = 10**5
    if N < n_min or N > n_max: raise AssertionError
    def is_valid(v):
        valid = True
        if not isinstance(v,int): valid = False
        val_min = -10**3
        val_max = 10**3
        if v < val_min or v > val_max: valid = False
        return valid
    diff = []
    c1,c2 = 0,0
    start = True
    for i in range(N-1):
        if start:
            if not is_valid(A[i]): raise AssertionError
        c1 += A[i]
        for j in range(i+1,N):
            if start:
                if not is_valid(A[j]): raise AssertionError
            c2 += A[j]
        diff.append(abs(c1-c2))
        c2 = 0
        start = False
    return min(diff)
