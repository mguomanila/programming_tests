'''
RESPECTABLE
[50%] MinAvgTwoSlice
START
Find the minimal average of any slice containing at least two elements.
Programming language:  
A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

For example, array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
contains the following example slices:

slice (1, 2), whose average is (2 + 2) / 2 = 2;
slice (3, 4), whose average is (5 + 1) / 2 = 3;
slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
The goal is to find the starting position of a slice whose average is minimal.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the starting position of the slice with the minimal average. If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.

For example, given array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−10,000..10,000].
'''
from timeit import timeit
from random import randrange as r
from statistics import mean


def soln(P,C):
    valid = True
    lower = 1
    upper = int(3e4)
    if not isinstance(P,int) or not isinstance(C,int): valid = False
    if valid: # test again
        if P < lower or P > upper or C < lower or C > upper: valid = False
    if not valid: raise AssertionError
    # find answer
    A,B = divmod(P,2)
    if A > C: answer = C
    else:
        answer = A
    return answer

# find the minimal avg of any slice containing at least two elements
def soln1(A):
    N = len(A)
    avg = []
    avg_min = []
    for i in range(N-1):
        prev = 0
        start = True
        for j in range(i+1,N):
            if start:
                prev += (A[i]+A[j])/(j+1)
                start = False
            else:
                prev += A[j]/(j+1)
            avg.append(prev)
        avg_min.append((i,min(avg)))
    key = min([b for _,b in avg_min])
    ans = 0
    for a,b in avg_min:
        if b == key:
            ans = a
    #print(ans)
    return ans

def soln2(A):
    N = len(A)
    avg = []
    avg_min = {}
    for i in range(N-1):
        prev = 0 
        start = True
        for j in range(i+1,N):
            if start:
                prev = (A[i]+A[j])/(j+1)
                start = False
            else: 
                prev += (A[i]+A[j])/(j+1)
            avg.append(prev)
        avg_min.update({i:min(avg)})
    key = min([a for a in avg_min.values()])
    ans = 0
    for a,b in avg_min.items():
        if b == key:
            ans = a
    #print(ans)
    return ans

def soln3(A):
    n = len(A)
    avg = []
    avg_list = []
    count = 0
    avg_min = 0
    index = 0
    while count < n-1:
        for i in range(count,n):
            if not len(avg):
                avg +=[A[i]]
            else:
                avg += [A[i]]
                avg_list += [mean(avg)]
        a = min(avg_list)
        if not avg_min:
            avg_min = a
        if avg_min > a:
            avg_min = a
            index = count
        avg = []
        avg_list = []
        count += 1    
    return index

def soln4(A):
    pass

if __name__ == '__main__':
    n_max = 10**3
    v_min = -10**3
    v_max = 10**3
    A = [r(v_min,v_max) for a in range(n_max)]
    #a = timeit('soln1(A)',number=10**1,globals=globals()) # 40.69347991900577s
    #b = timeit('soln2(A)',number=10**1,globals=globals()) # 39.90675353498955s
    c = timeit('soln3(A)',number=10**1,globals=globals()) 
