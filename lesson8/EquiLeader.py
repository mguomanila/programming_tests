'''
EquiLeader
START
Find the index S such that the leaders of the sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N - 1] are the same.
Programming language:  
A non-empty array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

For example, given array A such that:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
we can find two equi leaders:

0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
The goal is to count the number of equi leaders.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the number of equi leaders.

For example, given:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
the function should return 2, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].
'''
from timeit import timeit
from random import randrange as r
from array import array


def soln1(A):
    n = len(A)
    leader = []
    for i in range(n-1):
        if A[i] not in (a for a,_ in leader):
            leader.append([A[i],0])
            for j in range(i+1,n):
                if leader[-1][0] == A[j]:
                    leader[-1][1] += 1
    count = 0
    index = 0
    for i in range(len(leader)):
        if i==0:
            pass
        else:
            if count > leader[i][1]: continue
        count = leader[i][1]
        index = leader[i][0]
    return A[index]


def soln2(A):
    N = len(A)
    n_min = 0
    n_max = 10**5
    if N < n_min or N > n_max: raise AssertionError
    leader = {}
    for i in range(N-1):
        if A[i] not in leader:
            leader.update({A[i]:0})
            for j in range(i+1,N):
                if A[i] == A[j]:
                    leader[A[i]] += 1
    den = max(a for a in leader.values())
    return den


def soln3(A):
    # write your code in Python 3.6
    n = len(A)
    AA = sorted(A)
    index = n // 2
    try:
        candidate = AA[index]
    except:
        return -1
    count = 0
    for i in range(n):
        if AA[i] == candidate:
            count += 1
        if i > index and AA[i] != candidate: break
    
    equi_count = 0
    if count > index:
        # count equileader
        for i in range(index):
            if A[i] != candidate: continue
            else: equi_count += 1
        return equi_count
    else:
        return -1


if __name__ == '__main__':
    n_min = 1
    n_max = 10**5
    a_min = -10**9
    a_max = 10**9
    A = [r(a_min,a_max) for a in range(n_max)]
    a = timeit('soln3(A)',number=10**0,globals=globals()) # 0.04221807900466956
    #print('#1',a)
    #soln1([3, 4, 3, 2, 3, -1, 3, 3])
    
