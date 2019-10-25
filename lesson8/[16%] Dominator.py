'''
[16%] Dominator
START
Find an index of an array such that its value occurs at more than half of indices in the array.
Programming language:  Spoken language:  
An array A consisting of N integers is given. The dominator of array A is the value that occurs in more than half of the elements of A.

For example, consider array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.

Write a function

def solution(A)

that, given an array A consisting of N integers, returns index of any element of array A in which the dominator of A occurs. The function should return −1 if array A does not have a dominator.

For example, given array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
the function may return 0, 2, 4, 6 or 7, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].

''' 
'''
Test Score
91 out of 100 points -> 91%

Tasks in Test
Time Spent 33 min
Task Score 91%

Dominator
Submitted in: Python

extreme_empty_and_single_item 
empty and single element arrays ✘RUNTIME ERROR 
tested program terminated with exit code 1
1. 0.044 s RUNTIME ERROR,  tested program terminated with exit code 1
stderr:
Traceback (most recent call last):
  File "exec.py", line 129, in <module>
    main()
  File "exec.py", line 91, in main
    result = solution( A )
  File "/tmp/solution.py", line 9, in solution
    dom = AA[index]
IndexError: list index out of range
2. 0.036 s OK
'''
from timeit import timeit
from random import randrange as r

# perfect score!
def soln1(A):
    # write your code in Python 3.6
    n = len(A)
    AA = sorted(A)
    index = n // 2
    try:
        dom = AA[index]
    except:
        return -1
    count = 0
    for no in AA:
        if dom == no:
            count += 1
    if count > index:
        return A.index(dom)
    else:
        return -1
    
    
if __name__ == '__main__':
    n_min = 0
    n_max = 10**5
    a_min = -2147483648
    a_max = 2147483648
    A = [r(a_min,a_max) for a in range(n_max)]
    a = timeit('soln1(A)',number=10**0,globals=globals()) # 0.04300316600711085
    A = [-1,1,0]
    b = soln1(A)
    
