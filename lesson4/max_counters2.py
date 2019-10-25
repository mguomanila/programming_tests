'''

'''
def solution(N, A):
    # write your code in Python 3.6
    pass
    
    m = len(A)
    n_min = 1
    n_max = 10**5
    if N < n_min or N > n_max or m < n_min or m > n_max: raise AssertionError
    if max(A) > N+1: raise AssertionError
    from array import array
    try:
        A = array('H',A)
        counter = array('H',[0 for a in range(N)])
    except:
        raise AssertionError
    def inc(X):
        nonlocal counter
        if X <= N:
            counter[X-1] += 1
        elif X > N:
            r = max(counter)
            counter = array('H',[r for a in range(N)])
    for v in A:
        inc(v)
    return list(counter)

def solution2(N, A):
    # write your code in Python 3.6
    pass
    
    m = len(A)
    n_min = 1
    n_max = 10**5
    if N < n_min or N > n_max or m < n_min or m > n_max: raise AssertionError
    if max(A) > N+1: raise AssertionError
    from array import array
    try:
        A = array('H',A)
    except:
        raise AssertionError
    counter = array('H', [0 for a in range(N)])
    for X in A:
        if X <= N:
            counter[X-1] += 1
        elif X > N:
            r = max(counter)
            counter = array('H', [r for a in range(N)])
    return counter
