'''
[75%] Brackets
START
Determine whether a given string of parentheses (multiple types) is properly nested.
Programming language:  
A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

S is empty;
S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

def solution(S)

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..200,000];
string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".
'''
from random import randrange as r
from timeit import timeit
from array import array


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def soln1(S):
    # write your code in Python 3.6
    '''
    N = len(S)
    n_min = 0
    n_max = 2*10**5
    if N < n_min or N > n_max: raise AssertionError
    
    valid = (1 if a in t1 or a in t2 else 0 for a in S)
    if not all(valid): raise AssertionError
    '''
    t1 = '{[('
    t2 = '}])'
    S = list(S)
    while True:
        N = len(S)
        for i in range(N):
            if i == 0:
                if S[i] in t2: 
                    return 0
            elif S[i] in t2: # bracket close
                index = t2.index(S[i])
                if S[i-1]+S[i] == t1[index]+t2[index]:
                    del (S[i-1:i+1])
                    break
        else:
            if N != 0: return 0
            break
    return 1


def soln2(S):
    # write your code in Python 3.6
    '''
    N = len(S)
    n_min = 0
    n_max = 2*10**5
    if N < n_min or N > n_max: raise AssertionError
    
    valid = (1 if a in t1 or a in t2 else 0 for a in S)
    if not all(valid): raise AssertionError
    '''
    t1 = '{[('
    t2 = '}])'
    S = array('u', (a for a in S))
    while True:
        N = len(S)
        for i in range(N):
            if i == 0:
                if S[i] in t2: 
                    return 0
            elif S[i] in t2: # bracket close
                index = t2.index(S[i])
                if S[i-1]+S[i] == t1[index]+t2[index]:
                    del (S[i-1:i+1])
                    break
        else:
            if N != 0: return 0
            break
    return 1

def soln3(S):
    t1 = '{[('
    t2 = '}])'
    N = len(S)
    n_min = 0
    n_max = 2*10**5
    if N < n_min or N > n_max: raise AssertionError
    while True:
        N = len(S)
        for i in range(N):
            if i == 0:
                if S[i] in t2: 
                    return 0
            elif S[i] in t2: # bracket close
                index = t2.index(S[i])
                if S[i-1]+S[i] == t1[index]+t2[index]:
                    S = S[:i-1] + S[i+1:]
                    break
        else:
            if N != 0: return 0
            break
    return 1

def soln4(S):
    while "\{\}" in S or '[]' in S or '()' in S:
        S = S.replace("\{\}", "").replace('[]','').replace('()','')
    if len(S) > 0:
        return 0
    else:
        return 1
    
def soln5(S):
    while "\{\}" in S:
        S = S.replace("\{\}", "")
    while '[]' in S:
        S = S.replace('[]','')
    while '()' in S:
        S = S.replace('()','')
    if len(S) > 0:
        return 0
    else:
        return 1
    


if __name__ == '__main__':
    s = '{[()]}'
    '''
    a = timeit('soln1("".join(s[r(0,6)] for a in range(12*10**3)))',number=10,globals=globals())
    print('1#',a)
    a = timeit('soln2("".join(s[r(0,6)] for a in range(12*10**3)))',number=10,globals=globals())
    print('2#',a)
    a = timeit('soln3("".join(s[r(0,6)] for a in range(12*10**3)))',number=10,globals=globals())
    print('3#',a)
    '''
    a = timeit('soln4("".join(s[r(0,6)] for a in range(12*10**4)))',number=10,globals=globals())
    print('4#',a)
    a = timeit('soln5("".join(s[r(0,6)] for a in range(12*10**4)))',number=10,globals=globals())
    print('5#',a)
