'''
[54%] FrogRiverOne
VIEW START

A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river (position 0) and wants to get to the opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.

You are given an array A consisting of N integers representing the falling leaves. A[K] represents the position where one leaf falls at time K, measured in seconds.

The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only when leaves appear at every position across the river from 1 to X (that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves). You may assume that the speed of the current in the river is negligibly small, i.e. the leaves do not change their positions once they fall in the river.

For example, you are given integer X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.

Write a function:

def solution(X, A)

that, given a non-empty array A consisting of N integers and integer X, returns the earliest time when the frog can jump to the other side of the river.

If the frog is never able to jump to the other side of the river, the function should return −1.

For example, given X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
the function should return 6, as explained above.

Write an efficient algorithm for the following assumptions:

N and X are integers within the range [1..100,000];
each element of array A is an integer within the range [1..X].

'''
from timeit import timeit
from random import randrange as r


def soln1(X,A):
    N = len(A)
    upper_limit = 10**5
    lower_limit = 1
    if not isinstance(X,int): raise AssertionError
    if not N or N < lower_limit or N > upper_limit: raise AssertionError
    for num in A:
        if not isinstance(num,int) or num < lower_limit or num > upper_limit: 
            raise AssertionError
    step = []
    for sec in range(N):
        step.append(A[sec])
        if A[sec] == X:
            temp = set(step)
            count = 0
            for check in temp:
                if check > 0:
                    if (check-1) != count: break
                count = check
            else:
                return sec
    else:
        return -1
    

def soln2(X,A):
    n = len(A)
    n_min = 1
    n_max = 10**5
    if n < n_min or n > n_max or X < n_min or X > n_max: raise AssertionError
    v_min = min(A)
    v_max = max(A)
    time = -1
    if v_min != 1 or X > n or X > v_max: return time
    counter = []
    for a,b in enumerate(A):
        if b not in counter:
            counter += [b]
        #print(counter,v_max,b,max(counter))
        if len(counter) >= X and max(counter) == X:
            time = a
            break
    return time


def soln3(X,A):
    N = len(A)
    n_min = 1
    n_max = 10**5
    if N < n_min or N > n_max or X < n_min or X > n_max: raise AssertionError
    v_min = min(A)
    v_max = max(A)
    if v_min != 1 or X > n or X > v_max: return -1
    sampling = []
    for i in range(N):
        if A[i] not in sampling:
            sampling.append(A[i])
    if len(sampling) >= X and max(sampling) == X:
        return i
    
def soln4(X,A):
    N = len(A)
    sampling = []
    timer = -1
    for i in range(N):
        if A[i] not in sampling:
            sampling.append(A[i])
        if X  <= len(sampling) and X == max(sampling):
            time = i
            break
    return timer


def soln5(X,A):
    N = len(A)
    sampling = []
    timer = -1
    for i in range(N):
        if A[i] not in sampling:
            sampling += [A[i]]
        if X  <= len(sampling) and X == max(sampling):
            time = i
            break
    return timer


if __name__ =='__main__':
    n_min = 1
    n_max = 5*10**3
    X = 2
    A = [1, 1, 1, 1]
    rr = [r(n_min,n_max) for a in range(n_max)]
    xx = r(n_min,n_max)
    #a = timeit('soln3(xx,rr)',number=10**1,globals=globals())
    #b = timeit('soln2(xx,rr)',number=10**1,globals=globals())
    #c = timeit('soln1(xx,rr)',number=10**1,globals=globals())
    c = timeit('soln4(xx,rr)',number=10**1,globals=globals())
    d = timeit('soln5(xx,rr)',number=10**1,globals=globals())
    #%timeit soln1(xx,rr)
    #%timeit soln2(xx,rr)
    #%timeit soln3(xx,rr)
