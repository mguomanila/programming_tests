'''
NailingPlanks
Count the minimum number of nails that allow a series of planks to be nailed.

You are given two non-empty arrays A and B consisting of N integers. These arrays represent N planks. More precisely, A[K] is the start and B[K] the end of the K−th plank.

Next, you are given a non-empty array C consisting of M integers. This array represents M nails. More precisely, C[I] is the position where you can hammer in the I−th nail.

We say that a plank (A[K], B[K]) is nailed if there exists a nail C[I] such that A[K] ≤ C[I] ≤ B[K].

The goal is to find the minimum number of nails that must be used until all the planks are nailed. In other words, you should find a value J such that all planks will be nailed after using only the first J nails. More precisely, for every plank (A[K], B[K]) such that 0 ≤ K < N, there should exist a nail C[I] such that I < J and A[K] ≤ C[I] ≤ B[K].

For example, given arrays A, B such that:

    A[0] = 1    B[0] = 4
    A[1] = 4    B[1] = 5
    A[2] = 5    B[2] = 9
    A[3] = 8    B[3] = 10
four planks are represented: [1, 4], [4, 5], [5, 9] and [8, 10].

Given array C such that:

    C[0] = 4
    C[1] = 6
    C[2] = 7
    C[3] = 10
    C[4] = 2
if we use the following nails:

0, then planks [1, 4] and [4, 5] will both be nailed.
0, 1, then planks [1, 4], [4, 5] and [5, 9] will be nailed.
0, 1, 2, then planks [1, 4], [4, 5] and [5, 9] will be nailed.
0, 1, 2, 3, then all the planks will be nailed.
Thus, four is the minimum number of nails that, used sequentially, allow all the planks to be nailed.

Write a function:

class Solution { public int solution(int[] A, int[] B, int[] C); }

that, given two non-empty arrays A and B consisting of N integers and a non-empty array C consisting of M integers, returns the minimum number of nails that, used sequentially, allow all the planks to be nailed.

If it is not possible to nail all the planks, the function should return −1.

For example, given arrays A, B, C such that:

    A[0] = 1    B[0] = 4
    A[1] = 4    B[1] = 5
    A[2] = 5    B[2] = 9
    A[3] = 8    B[3] = 10

    C[0] = 4
    C[1] = 6
    C[2] = 7
    C[3] = 10
    C[4] = 2
the function should return 4, as explained above.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..30,000];
each element of arrays A, B, C is an integer within the range [1..2*M];
A[K] ≤ B[K].
''' 
'''
Analysis summary
The following issues have been detected: wrong answers, timeout errors.

For example, for the input ([2], [2], [1]) the solution returned a wrong answer (got 0 expected -1).
Example tests
▶ example 
example test ✔OK
1. 0.036 s OK
collapse allCorrectness tests
▶ extreme_single 
single nail and single plank ✘WRONG ANSWER 
got 0 expected -1
1. 0.036 s OK
2. 0.036 s WRONG ANSWER,  got 0 expected -1
▶ extreme_point 
nail is a point [1, 1] ✘WRONG ANSWER 
got 0 expected -1
1. 0.036 s OK
2. 0.040 s WRONG ANSWER,  got 0 expected -1
▶ few_nails_in_the_same_place 
few nails are in the same place ✘WRONG ANSWER 
got 5 expected 2
1. 0.036 s WRONG ANSWER,  got 5 expected 2
2. 0.036 s WRONG ANSWER,  got 5 expected 3
3. 0.036 s WRONG ANSWER,  got 5 expected 1
▶ random_small 
random sequence, length = ~100 ✘WRONG ANSWER 
got 100 expected 61
1. 0.036 s WRONG ANSWER,  got 100 expected 61
'''
'''
Performance tests
▶ random_medium 
random sequence, length = ~10,000 ✘WRONG ANSWER 
got 10000 expected 7827
1. 0.088 s WRONG ANSWER,  got 10000 expected 7827
2. 0.172 s WRONG ANSWER,  got 30000 expected 6566
▶ random_large 
random sequence, length = ~30,000 ✘TIMEOUT ERROR 
running time: >7.00 sec., time limit: 1.47 sec.
1. 7.000 s TIMEOUT ERROR,  running time: >7.00 sec., time limit: 1.47 sec.
▶ extreme_large_planks 
all large planks, length = ~30,000 ✘TIMEOUT ERROR 
running time: >7.00 sec., time limit: 1.33 sec.
1. 7.000 s TIMEOUT ERROR,  running time: >7.00 sec., time limit: 1.33 sec.
▶ large_point 
all planks are points, length = ~30,000 ✘TIMEOUT ERROR 
running time: >7.00 sec., time limit: 1.50 sec.
1. 7.000 s TIMEOUT ERROR,  running time: >7.00 sec., time limit: 1.50 sec.
'''
def soln1(A, B, C):
    # write your code in Python 3.6
    n = len(A) # planks
    m = len(C) # nails
    cp = 0
    for i in range(n):
        for j in range(m):
            if A[i] <= C[j] <= B[i]:
                cp += 1
                break
    if not cp: return -1
    else: return cp

def soln2(A,B,C):
    n = len(A) # planks
    m = len(C) # nails
    cp = 0
    for i in range(m):
        j = 0
        while j < len(A):
            if A[j] <= C[i] <= B[j]:
                A.pop(j)
                B.pop(j)
                if not len(A):
                    cp += 1
                    break
            else: 
                j += 1
                if len(A) < n:
                    n = len(A)
                    cp += 1
            if not len(A): break
        if not len(A): break
    if not cp: return -1
    else: return cp


from random import randint as r
from timeit import timeit

if __name__ == '__main__':
    n_min = 1
    n_max = 3*10**4
    v_max = 2*n_max
    vmid = v_max // 2
    #n_range = r(n_min,n_max)
    A = [r(n_min,vmid-1) for a in range(n_max)]
    B = [r(vmid,v_max) for a in range(n_max)]
    C = [r(n_min,n_max) for a in range(r(n_min,n_max))]
    print('AA',len(A))
    a = timeit("soln2(A,B,C)",number=1,globals=globals())
    print('AA',len(A))
    b = soln2([2], [2], [1])
    c = soln2([1,2], [1,2], [1,1])
    d = soln2([1,4,5,8],[4,5,9,10],[4,6,7,10,2]) # 4
    e = soln2([1], [2], [2]) # 1
