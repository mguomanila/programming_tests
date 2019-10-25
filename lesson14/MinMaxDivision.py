'''


You are given integers K, M and a non-empty array A consisting of N integers. Every element of the array is not greater than M.

You should divide this array into K blocks of consecutive elements. The size of the block is any integer between 0 and N. Every element of the array should belong to some block.

The sum of the block from X to Y equals A[X] + A[X + 1] + ... + A[Y]. The sum of empty block equals 0.

The large sum is the maximal sum of any block.

For example, you are given integers K = 3, M = 5 and array A such that:
  A[0] = 2
  A[1] = 1
  A[2] = 5
  A[3] = 1
  A[4] = 2
  A[5] = 2
  A[6] = 2

The array can be divided, for example, into the following blocks:

        [2, 1, 5, 1, 2, 2, 2], [], [] with a large sum of 15;
        [2], [1, 5, 1, 2], [2, 2] with a large sum of 9;
        [2, 1, 5], [], [1, 2, 2, 2] with a large sum of 8;
        [2, 1], [5, 1], [2, 2, 2] with a large sum of 6.

The goal is to minimize the large sum. In the above example, 6 is the minimal large sum.

Write a function:

    def solution(K, M, A)

that, given integers K, M and a non-empty array A consisting of N integers, returns the minimal large sum.

For example, given K = 3, M = 5 and array A such that:
  A[0] = 2
  A[1] = 1
  A[2] = 5
  A[3] = 1
  A[4] = 2
  A[5] = 2
  A[6] = 2

the function should return 6, as explained above.

Write an efficient algorithm for the following assumptions:

        N and K are integers within the range [1..100,000];
        M is an integer within the range [0..10,000];
        each element of array A is an integer within the range [0..M].


'''
from timeit import timeit
from random import randrange as r
from array import array
from bisect import bisect


def soln1(K, M, A):
    # write your code in Python 3.6
    n = len(A)
    a = []
    for i in range(1,n-K):
        for j in range(1,K):
            a += [max([sum(A[:j]),sum(A[j:j+i]),sum(A[j+i:])])]
            #print(a)
    return min(a)


def soln2(K,M,A):
    n = len(A)
    a = array('I',[])
    for i in range(1,n-K):
        for j in range(1,K):
            a.append(max([sum(A[:j]),sum(A[j:j+i]),sum(A[j+i:])]))
    return min(a)

def soln3(k,M,A):
    n = len(A)
    nn = n-K
    block = []
    for i in range(n):
        for j in range(K):
            a = sum(A[:i+j])
            b = sum(A[j+1:+K])
            c = sum(A[i+3:])
            block.append(max([a,b,c]))
    return min(block)

def check(A,k):
    pass

def soln4(k,M,A):
    # write your code in Python 3.6
    n = len(A)
    if K > 1: nn = 2
    else: nn = K
    stack = []
    for i in range(n):
        for j in range(K):
            a = sum(A[:j+1])
            b = sum(A[j+1:j+nn+1])
            c = sum(A[j+nn+1:])
            stack.append(max([a,b,c]))
    return min(stack)
    
'''
extreme_single 
single elements ✘RUNTIME ERROR 
tested program terminated with exit code 1
1. 0.036 s RUNTIME ERROR,  tested program terminated with exit code 1
stderr:
Traceback (most recent call last):
  File "exec.py", line 137, in <module>
    main()
  File "exec.py", line 99, in main
    result = solution( K, M, A )
  File "/tmp/solution.py", line 15, in solution
    return min(block)
ValueError: min() arg is an empty sequence
2. 0.036 s RUNTIME ERROR,  tested program terminated with exit code 1
stderr:
Traceback (most recent call last):
  File "exec.py", line 137, in <module>
    main()
  File "exec.py", line 99, in main
    result = solution( K, M, A )
  File "/tmp/solution.py", line 15, in solution
    return min(block)
ValueError: min() arg is an empty sequence
3. 0.036 s RUNTIME ERROR,  tested program terminated with exit code 1
stderr:
Traceback (most recent call last):
  File "exec.py", line 137, in <module>
    main()
  File "exec.py", line 99, in main
    result = solution( K, M, A )
  File "/tmp/solution.py", line 15, in solution
    return min(block)
ValueError: min() arg is an empty sequence
4. 0.036 s RUNTIME ERROR,  tested program terminated with exit code 1
stderr:
Traceback (most recent call last):
  File "exec.py", line 137, in <module>
    main()
  File "exec.py", line 99, in main
    result = solution( K, M, A )
  File "/tmp/solution.py", line 15, in solution
    return min(block)
ValueError: min() arg is an empty sequence
'''
'''
extreme_double 
single and double elements ✘RUNTIME ERROR 
tested program terminated with exit code 1
1. 0.036 s RUNTIME ERROR,  tested program terminated with exit code 1
stderr:
Traceback (most recent call last):
  File "exec.py", line 137, in <module>
    main()
  File "exec.py", line 99, in main
    result = solution( K, M, A )
  File "/tmp/solution.py", line 15, in solution
    return min(block)
ValueError: min() arg is an empty sequence
2. 0.036 s RUNTIME ERROR,  tested program terminated with exit code 1
stderr:
Traceback (most recent call last):
  File "exec.py", line 137, in <module>
    main()
  File "exec.py", line 99, in main
    result = solution( K, M, A )
  File "/tmp/solution.py", line 15, in solution
    return min(block)
ValueError: min() arg is an empty sequence
3. 0.036 s RUNTIME ERROR,  tested program terminated with exit code 1
stderr:
Traceback (most recent call last):
  File "exec.py", line 137, in <module>
    main()
  File "exec.py", line 99, in main
    result = solution( K, M, A )
  File "/tmp/solution.py", line 15, in solution
    return min(block)
ValueError: min() arg is an empty sequence
4. 0.036 s RUNTIME ERROR,  tested program terminated with exit code 1
stderr:
Traceback (most recent call last):
  File "exec.py", line 137, in <module>
    main()
  File "exec.py", line 99, in main
    result = solution( K, M, A )
  File "/tmp/solution.py", line 15, in solution
    return min(block)
ValueError: min() arg is an empty sequence
5. 0.036 s RUNTIME ERROR,  tested program terminated with exit code 1
stderr:
Traceback (most recent call last):
  File "exec.py", line 137, in <module>
    main()
  File "exec.py", line 99, in main
    result = solution( K, M, A )
  File "/tmp/solution.py", line 15, in solution
    return min(block)
ValueError: min() arg is an empty sequence
6. 0.036 s RUNTIME ERROR,  tested program terminated with exit code 1
stderr:
Traceback (most recent call last):
  File "exec.py", line 137, in <module>
    main()
  File "exec.py", line 99, in main
    result = solution( K, M, A )
  File "/tmp/solution.py", line 15, in solution
    return min(block)
ValueError: min() arg is an empty sequence
'''
'''
extreme_min_max 
maximal / minimal values ✘WRONG ANSWER 
got 10000 expected 20000
1. 0.036 s WRONG ANSWER,  got 10000 expected 20000
2. 0.036 s WRONG ANSWER,  got 20000 expected 30000
3. 0.036 s OK
4. 0.036 s RUNTIME ERROR,  tested program terminated with exit code 1
stderr:
Traceback (most recent call last):
  File "exec.py", line 137, in <module>
    main()
  File "exec.py", line 99, in main
    result = solution( K, M, A )
  File "/tmp/solution.py", line 15, in solution
    return min(block)
ValueError: min() arg is an empty sequence
'''
'''
simple1 
simple tests ✘RUNTIME ERROR 
tested program terminated with exit code 1
1. 0.036 s OK
2. 0.036 s RUNTIME ERROR,  tested program terminated with exit code 1
stderr:
Traceback (most recent call last):
  File "exec.py", line 137, in <module>
    main()
  File "exec.py", line 99, in main
    result = solution( K, M, A )
  File "/tmp/solution.py", line 15, in solution
    return min(block)
ValueError: min() arg is an empty sequence
3. 0.036 s OK
'''
'''
simple2 
simple tests ✘WRONG ANSWER 
got 9 expected 7
1. 0.036 s WRONG ANSWER,  got 9 expected 7
2. 0.036 s RUNTIME ERROR,  tested program terminated with exit code 1
stderr:
Traceback (most recent call last):
  File "exec.py", line 137, in <module>
    main()
  File "exec.py", line 99, in main
    result = solution( K, M, A )
  File "/tmp/solution.py", line 15, in solution
    return min(block)
ValueError: min() arg is an empty sequence
3. 0.036 s WRONG ANSWER,  got 15 expected 11
'''
'''
tiny_random_ones 
random values {0, 1}, N = 100 ✘WRONG ANSWER 
got 4 expected 8
1. 0.036 s WRONG ANSWER,  got 4 expected 8
2. 0.036 s OK
3. 0.036 s WRONG ANSWER,  got 4 expected 3
4. 0.036 s WRONG ANSWER,  got 4 expected 2
'''
'''
Correctness tests
▶ extreme_single 
single elements ✔OK
1. 0.036 s OK
2. 0.036 s OK
3. 0.036 s OK
4. 0.048 s OK
▶ extreme_double 
single and double elements ✘WRONG ANSWER 
got 5 expected 8
1. 0.036 s WRONG ANSWER,  got 5 expected 8
2. 0.036 s OK
3. 0.036 s OK
4. 0.036 s OK
5. 0.036 s OK
6. 0.036 s OK
▶ extreme_min_max 
maximal / minimal values ✘WRONG ANSWER 
got 10000 expected 20000
1. 0.036 s WRONG ANSWER,  got 10000 expected 20000
2. 0.036 s WRONG ANSWER,  got 10000 expected 30000
3. 0.036 s OK
4. 0.084 s OK
▶ simple1 
simple tests ✔OK
1. 0.036 s OK
2. 0.036 s OK
3. 0.036 s OK
▶ simple2 
simple tests ✘WRONG ANSWER 
got 1998 expected 999
1. 0.036 s OK
2. 0.036 s WRONG ANSWER,  got 1998 expected 999
3. 0.036 s WRONG ANSWER,  got 13 expected 11
▶ tiny_random_ones 
random values {0, 1}, N = 100 ✘WRONG ANSWER 
got 7 expected 4
1. 0.040 s OK
2. 0.040 s WRONG ANSWER,  got 7 expected 4
3. 0.036 s WRONG ANSWER,  got 6 expected 3
4. 0.036 s WRONG ANSWER,  got 5 expected 2
collapse allPerformance tests
▶ small_random_ones 
random values {0, 1}, N = 100 ✘WRONG ANSWER 
got 52 expected 27
1. 0.036 s OK
2. 0.036 s WRONG ANSWER,  got 52 expected 27
3. 0.040 s WRONG ANSWER,  got 51 expected 18
4. 0.044 s WRONG ANSWER,  got 40 expected 3
▶ medium_zeros 
many zeros and 99 in the middle, length = 15,000 ✘TIMEOUT ERROR 
running time: 3.00 sec., time limit: 0.34 sec.
1. 3.004 s TIMEOUT ERROR,  running time: 3.00 sec., time limit: 0.34 sec.
2. 6.000 s TIMEOUT ERROR,  running time: >6.00 sec., time limit: 0.34 sec.
3. 6.000 s TIMEOUT ERROR,  running time: >6.00 sec., time limit: 0.34 sec.
4. 6.000 s TIMEOUT ERROR,  running time: >6.00 sec., time limit: 0.32 sec.
▶ medium_random 
random values {1, 100}, N = 20,000 ✘TIMEOUT ERROR 
running time: >6.00 sec., time limit: 0.43 sec.
1. 6.000 s TIMEOUT ERROR,  running time: >6.00 sec., time limit: 0.43 sec.
2. 6.000 s TIMEOUT ERROR,  running time: >6.00 sec., time limit: 0.43 sec.
3. 6.000 s TIMEOUT ERROR,  running time: >6.00 sec., time limit: 0.43 sec.
4. 6.000 s TIMEOUT ERROR,  running time: >6.00 sec., time limit: 0.42 sec.
▶ large_random 
random values {0, ..., MAX_INT}, N = 100,000 ✘TIMEOUT ERROR 
running time: >7.00 sec., time limit: 1.98 sec.
1. 7.000 s TIMEOUT ERROR,  running time: >7.00 sec., time limit: 1.98 sec.
2. 7.000 s TIMEOUT ERROR,  running time: >7.00 sec., time limit: 1.97 sec.
3. 8.000 s TIMEOUT ERROR,  running time: >8.00 sec., time limit: 2.02 sec.
4. 8.000 s TIMEOUT ERROR,  running time: >8.00 sec., time limit: 2.08 sec.
▶ large_random_ones 
random values {0, 1}, N = 100,000 ✘TIMEOUT ERROR 
running time: >7.00 sec., time limit: 1.41 sec.
1. 7.000 s TIMEOUT ERROR,  running time: >7.00 sec., time limit: 1.41 sec.
2. 7.000 s TIMEOUT ERROR,  running time: >7.00 sec., time limit: 1.47 sec.
3. 7.000 s TIMEOUT ERROR,  running time: >7.00 sec., time limit: 1.30 sec.
4. 7.000 s TIMEOUT ERROR,  running time: >7.00 sec., time limit: 1.26 sec.
▶ all_the_same 
all the same values, N = 100,000 ✘TIMEOUT ERROR 
running time: >8.00 sec., time limit: 2.02 sec.
1. 8.000 s TIMEOUT ERROR,  running time: >8.00 sec., time limit: 2.02 sec.
2. 7.000 s TIMEOUT ERROR,  running time: >7.00 sec., time limit: 1.98 sec.
3. 7.000 s TIMEOUT ERROR,  running time: >7.00 sec., time limit: 1.95 sec.
4. 8.000 s TIMEOUT ERROR,  running time: >8.00 sec., time limit: 2.27 sec.
'''
if __name__ == '__main__':
    n_min = 1
    n_max = 10**5
    m_max = 10**4
    K = r(n_min,n_max)
    M = r(n_min,m_max)
    A = [r(n_min,M) for a in range(n_max)]
    #a = timeit('soln1(K, M, A)',number=1,globals=globals())
    #a = timeit('soln2(K, M, A)',number=1,globals=globals())
    #a = timeit('soln4(K, M, A)',number=1,globals=globals())
    b = soln3(3,5,[2,1,5,1,2,2,2])
    c = soln3(3,5,[2,1,2,1,2,5,2])
    d = soln4(1,0,[0])
    #e = soln4(1)
