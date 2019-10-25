from timeit import timeit
from array import array


# sieve of erastosthenes
def sieve1(n):
    sieve = [1] * (n+1)
    sieve[0] = sieve[1] = 0
    i = 2
    while i*i <= n:
        if sieve[i]:
            k = i*i
            while k <= n:
                sieve[k] = 0
                k += i
        i += 1
    return sieve

def sieve2(n):
    sieve = array('B', (1 for a in range(n+1)))
    sieve[0] = sieve[1] = 0
    i = 2
    while i*i <=n:
        if sieve[i]:
            k = i*i
            while k <= n:
                sieve[k] = 0
                k += i
        i += 1
    return sieve


def my_sieve1(n):
    sieve = array('I', (a for a in range(2,n+1)))
    val = sieve[-1]
    a = 1
    while a*a <= val:
        a += 1
        for i in range(a+a,val+1,a):
            try: sieve.remove(i)
            except: continue
    return sieve


def my_sieve2(n):
    sievex = array('B', sieve1(n))
    sievev = array('I', (a for a in range(n+1)))
    ar = array('I', ())
    for i in range(len(sievex)):
        if sievex[i]:
            ar.append(sievev[i])
    return ar


def my_sieve3(n):
    sievex = array('B', sieve2(n))
    sievev = array('I', (a for a in range(n+1)))
    ar = array('I', ())
    for i in range(len(sievex)):
        if sievex[i]:
            ar.append(sievev[i])
    return ar

def my_sieve4(n):
    sievex = sieve1(n)
    sievev = [a for a in range(n+1)]
    ar = []
    for i in range(len(sievex)):
        if sievex[i]:
            ar.append(sievev[i])
    return ar


# i think this is the fastest!
def my_sieve5(n):
    def yield_sieve(n):
        sievex = sieve1(n)
        sievev = [a for a in range(n+1)]
        for i in range(len(sievex)):
            if sievex[i]:
                yield sievev[i]
    return yield_sieve(n)


def my_factor():
    pass


def array_factor(n):
    F = [0] * (n+1)
    i = 2
    while i*i <= n:
        if F[i] == 0: 
            k = i*i
            while k <= n:
                if F[k] == 0:
                    F[k] = i
                k += i
        i += 1
    return F


# x --> O(logx)
def factorization(x,F):
    prime_factors = []
    while F[x] > 0:
        prime_factors += [F[x]]
        x = divmod(x,F[x])[0]
    prime_factors += [x]
    return prime_factors


def semi_primes(n,x,y):
    primes = find_primes(n)
    p = []
    for a,b in enumerate(primes): 
        if b >= x and b <= y:
            p.append(b)
    pp = set()
    n = len(p)
    for i in range(n-1):
        for j in range(i+1,n):
            pp.add(p[i]*p[j])
    return len(pp)


if __name__ == '__main__':
    #a = timeit('sieve(10**5)',number=10**1,globals=globals())
    #print('#1',a)
    #a = timeit('array_factor(10**5)',number=10**1,globals=globals())
    #print('#2',a)
    #a = timeit('factorization()',number=10**1,globals=globals())
    #print('#3',a)
    #a = timeit('my_sieve(10**2)',number=10**1,globals=globals())
    #print('#4 ashamed',a)
    #print(my_sieve(101))
    #a = timeit('my_sieve2(10**5)',number=10**2,globals=globals())
    #print('#5 wins!',a)
    #print(my_sieve2(101))
    #a = timeit('my_sieve3(10**5)',number=10**2,globals=globals())
    #print('#6',a)
    #print(my_sieve3(101))
    #a = timeit('my_sieve4(10**5)',number=10**2,globals=globals())
    #print('#6 contender',a)
    #print(my_sieve4(101))
    a = timeit('my_sieve5(10**5)',number=10**2,globals=globals())
    print('#7 wins! hands-down ',a)
    #print(my_sieve6(101))
    a = timeit('array_factor(10**5)',number=10**2,globals=globals())
    print('#8 factorization',a)
    
    a = []
    for i in range(m):
        a.append(semi_primes(N,P[i],Q[i]))
    return a
