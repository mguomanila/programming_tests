'''
[62%] GenomicRangeQuery
START
Find the minimal nucleotide from a range of sequence DNA.
Programming language:  
A DNA sequence can be represented as a string consisting of the letters A, C, G and T, which correspond to the types of successive nucleotides in the sequence. Each nucleotide has an impact factor, which is an integer. Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively. You are going to answer several queries of the form: What is the minimal impact factor of nucleotides contained in a particular part of the given DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters. There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers. The K-th query (0 ≤ K < M) requires you to find the minimal impact factor of nucleotides contained in the DNA sequence between positions P[K] and Q[K] (inclusive).

For example, consider string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
The answers to these M = 3 queries are as follows:

The part of the DNA between positions 2 and 4 contains nucleotides G and C (twice), whose impact factors are 3 and 2 respectively, so the answer is 2.
The part between positions 5 and 5 contains a single nucleotide T, whose impact factor is 4, so the answer is 4.
The part between positions 0 and 6 (the whole string) contains all nucleotides, in particular nucleotide A whose impact factor is 1, so the answer is 1.
Write a function:

def solution(S, P, Q)

that, given a non-empty string S consisting of N characters and two non-empty arrays P and Q consisting of M integers, returns an array consisting of M integers specifying the consecutive answers to all queries.

Result array should be returned as an array of integers.

For example, given the string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
the function should return the values [2, 4, 1], as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
M is an integer within the range [1..50,000];
each element of arrays P, Q is an integer within the range [0..N − 1];
P[K] ≤ Q[K], where 0 ≤ K < M;
string S consists only of upper-case English letters A, C, G, T.
'''

from timeit import timeit
from random import randrange



P = [2,5,0]
Q = [4,5,6]


def soln1(S,P,Q):
    valid = True
    lim_lower = 1
    valid_dna = 'ACGT'
    imp_fact = '1234'
    M = len(P)
    N = len(S)
    S = S.upper()
    def valid_string():
        nonlocal valid
        lim_upper = int(1e5)
        if N < lim_lower or N > lim_upper: valid = False
        if valid: # test again!
            valid = all(1 if s in valid_dna else 0 for s in S)
        return valid
    if not valid_string(): raise AssertionError
    def valid_array():
        nonlocal valid
        n_upper = int(5e4)
        if M != len(Q): valid = False
        if M < lim_lower or M > n_upper: valid = False
        def valid_arr(arr):
            nonlocal valid
            #print (valid)
            val_lower = 0
            counted = False
            key = 0
            for num in set(arr):
                if not isinstance(num, int): valid = False
                if num < val_lower or num > N: 
                    valid = False
                if not valid: break
            return valid
        if valid: # test again 
            valid = all(valid_arr(x) for x in (P,Q))
        if valid: # test again
            valid = all(P[k]<=Q[k] for k in range(M))
        return valid
    if not valid_array(): raise AssertionError
    # showtime!
    ans = []
    for i in range(M):
        p = P[i]
        q = Q[i]
        ans.append(min(imp_fact[valid_dna.find(S[x])] for x in range(p,q+1)))
    return ans



def soln2(S,P,Q):
    valid_dna = 'ACGT'
    imp_fact = '1234'
    n = len(S)
    m = len(P)
    if m != len(Q): raise AssertionError
    ans = []
    for i in range(m):
        p = P[i]
        q = Q[i]
        ans.append(int(min(imp_fact[valid_dna.find(S[x])] for x in range(p,q+1))))
    return ans



def solution(S, P, Q):
    # write your code in Python 3.6
    pass
    valid_dna = 'ACGT'
    imp_fact = [1,2,3,4]
    N = len(S)
    M = len(P)
    if M != len(Q): raise AssertionError
    n_min = 1
    n_max = 10**5
    if N < n_min or N > n_max: raise AssertionError
    m_min = 1
    m_max = 5*10**4
    if M < m_min or M > m_max: raise AssertionError
    if min(P) < 0 or min(Q) < 0: raise AssertionError
    if max(P) > N-1 or max(Q) > N-1: raise AssertionError
    S = S.upper()
    valid_str = (1 if a in S else 0 for a in valid_dna)
    if not all(valid_str): raise AssertionError
    ans =[]
    for i in range(M):
        p = P[i]
        q = Q[i]
        ans.append(min(imp_fact[valid_dna.index(S[x])] for x in range(p,q+1)))
    return ans


if __name__ == '__main__':
    dna = 'CAGCCTA'
    n_max = 10**5
    m_max = 5*10**4
    p_range = (0, (n_max/2)-1)
    q_range = (n_max/2, n_max)
    S = ''.join([dna[r(1,len(dna)]) for a in range(n_max)])
    P = [r(p_range[0],p_range[1]) for a in range(m_max)]
    Q = 
    a = timeit('solution(S,P,Q)',number=10**1,globals=globals())
