'''
[66%] MaxCounters
START
Calculate the values of counters after applying all alternating operations: increase counter by 1; set value of all counters to current maximum.
Programming language:  
You are given N counters, initially set to 0, and you have two possible operations on them:

increase(X) − counter X is increased by 1,
max counter − all counters are set to the maximum value of any counter.
A non-empty array A of M integers is given. This array represents consecutive operations:

if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.
For example, given integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the values of the counters after each consecutive operation will be:

    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
The goal is to calculate the value of every counter after all operations.

Write a function:

class Solution { public int[] solution(int N, int[] A); }

that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.

Result array should be returned as an array of integers.

For example, given:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the function should return [3, 2, 2, 4, 2], as explained above.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..100,000];
each element of array A is an integer within the range [1..N + 1].

'''

def soln(N,A):
    M = len(A)
    upper_limit = int(1e5)
    lower_limit = 1
    if not isinstance(N,int) or N < lower_limit or N > upper_limit: 
        raise AssertionError
    if not M or M < lower_limit or M > upper_limit: raise AssertionError
    for num in A:
        if not isinstance(num,int) or num < lower_limit or num > (N+1):
            raise AssertionError
    def inc(X,counter):
        if X <= N:
            counter[X-1] += 1
        else:
            max_count = max(counter)
            return [max_count for i in range(len(counter))]
        return counter
    counter = [0 for i in range(N)] # initialize counter
    for k in range(M):
        counter = inc(A[k],counter)
        #print (counter)
    return counter
