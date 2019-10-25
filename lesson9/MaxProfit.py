'''
MaxProfit
START
Given a log of stock prices compute the maximum possible earning.

An array A consisting of N integers is given. It contains daily prices of a stock share for a period of N consecutive days. If a single share was bought on day P and sold on day Q, where 0 ≤ P ≤ Q < N, then the profit of such transaction is equal to A[Q] − A[P], provided that A[Q] ≥ A[P]. Otherwise, the transaction brings loss of A[P] − A[Q].

For example, consider the following array A consisting of six elements such that:

  A[0] = 23171
  A[1] = 21011
  A[2] = 21123
  A[3] = 21366
  A[4] = 21013
  A[5] = 21367
If a share was bought on day 0 and sold on day 2, a loss of 2048 would occur because A[2] − A[0] = 21123 − 23171 = −2048. If a share was bought on day 4 and sold on day 5, a profit of 354 would occur because A[5] − A[4] = 21367 − 21013 = 354. Maximum possible profit was 356. It would occur if a share was bought on day 1 and sold on day 5.

Write a function,

def solution(A)

that, given an array A consisting of N integers containing daily prices of a stock share for a period of N consecutive days, returns the maximum possible profit from one transaction during this period. The function should return 0 if it was impossible to gain any profit.

For example, given array A consisting of six elements such that:

  A[0] = 23171
  A[1] = 21011
  A[2] = 21123
  A[3] = 21366
  A[4] = 21013
  A[5] = 21367
the function should return 356, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..400,000];
each element of array A is an integer within the range [0..200,000].
'''
from timeit import timeit
from random import randint as r

# score 55%
def soln1(A):
    n = len(A)
    profit = 0
    for i in range(n):
        for j in range(i+1,n):
            profit = max(profit, A[j]-A[i])
    if profit < 0:
        return 0
    else:
        return profit

def soln2(A):
    n = len(A)
    if n == 1 or not n: 
        return 0
    AQ,AP,profit = 0,0,0
    for i in range(n):
        AP = min(AP if not AP else a, a if AP < a else AP)
        AQ = max(AQ,a if < AQ else AQ)
        profit = max(profit,AQ-AP)
    if profit < 0:
        return 0
    else:
        return profit


if __name__ == '__main__':
    n_min = 0
    n_max = 4*10**5
    a_max = 2*10**5
    A = [r(n_min,a_max) for i in range(n_max)]
    #a = timeit('soln1(A)',number=10**0,globals=locals())
    a = timeit('soln2(A)',number=10**0,globals=locals())
    soln2([23171,21011,21123,21366,21013,21367])
