'''
[100%] MissingInteger
START
Find the smallest positive integer that does not occur in a given sequence.
Programming language:  
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
'''

def soln1(A):
    N = len(A)
    upper_limit = int(1e5)
    lower_limit = 1
    if N < lower_limit or N > upper_limit: raise AssertionError
    el_lower = -int(1e6)
    el_upper = int(1e6)
    for num in A:
        if num < el_lower or num > el_upper: raise AssertionError
    for num in A:
        if num > 0:
            break
    else:
        return 1
    key = 0
    A = list(set(A))
    print(A)
    for i in range(len(A)):
        if i == 0:
            if A[i] != 1:
                return 1
            else: key = A[i]
        else:
            if A[i] == (key+1):
                pass
            else: return (key+1)
        key = A[i]
    else:
        return (key+1)


def soln2(A):
    # write your code in Python 3.6
    N = len(A)
    n_min = 1
    n_max = 10**5
    if N < n_min or N > n_max: raise AssertionError
    v_min = -10**6
    v_max = 10**6
    va_min = min(A)
    va_max = max(A)
    if va_min < v_min or va_max > v_max: raise AssertionError
    if va_min > 1: 
        print('x')
        return 1
    from array import array
    try:
        A = array('i',A)
    except:
        raise AssertionError
    count = 1
    start = True
    for num in sorted(A):
        if start:
            start = False
        else:
            if num == count+1: pass
            elif num == count: pass
            elif num < 2: pass
            else: break
        count = num
    if count < 1: 
        count = 1
    else: count += 1
    return count
