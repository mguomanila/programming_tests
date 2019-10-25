''''
Task
Python

Two positive integers N and M are given. Integer N represents the number of chocolates arranged in a circle, numbered from 0 to N − 1.

You start to eat the chocolates. After eating a chocolate you leave only a wrapper.

You begin with eating chocolate number 0. Then you omit the next M − 1 chocolates or wrappers on the circle, and eat the following one.

More precisely, if you ate chocolate number X, then you will next eat the chocolate with number (X + M) modulo N (remainder of division).

You stop eating when you encounter an empty wrapper.

For example, given integers N = 10 and M = 4. You will eat the following chocolates: 0, 4, 8, 2, 6.

The goal is to count the number of chocolates that you will eat, following the above rules.

Write a function:

    def solution(N, M)

that, given two positive integers N and M, returns the number of chocolates that you will eat.

For example, given integers N = 10 and M = 4. the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

        N and M are integers within the range [1..1,000,000,000].

'''
from timeit import timeit
from random import randint as r
from array import array


def gcd(a,b):
    if not a % b:
        return b
    else:
        return gcd(b,a%b)


# 27.56175782799255sec
def soln1(N, M):
    # write your code in Python 3.6
    i = 0
    catch = array('L', [])
    while i not in catch:
        if i < N:
            catch.append(i)
            i += M
        else:
            i -= N
    #print(catch)
    return len(catch)
    

# 11.855960753979161secs
# Detected time complexity: O(N + M)
def soln2(N,M):
    counter = 0
    chocolate = []
    finished = False
    while not finished:
        while counter < N:
            if counter not in chocolate:
                chocolate.append(counter)
            else:
                finished = True
                break
            counter += M
        counter -= N
    return len(chocolate)    

# 7.059754996997071secs

def soln3(N,M):
    counter = 0
    chocolate = array('L',)
    finished = False
    while not finished:
        while counter < N:
            if counter not in chocolate:
                chocolate.append(counter)
            else:
                finished = True
                break
            counter += M
        counter -= N
    return len(chocolate) 

        
if __name__ == '__main__':
    n_min = 1
    n_max = 10**6
    N = r(n_min,n_max)
    M = r(n_min,N)
    a = timeit('soln2(N, M)',number=10**0,globals=locals())
    b = soln3(10,4)
