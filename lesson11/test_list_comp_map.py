from timeit import timeit
from random import randrange

if __name__ == '__main__':
    a = timeit('(ord(chr(randrange(0,10**3))) for a in range(10**5) if ord(chr(randrange(0,10**3))) < 10**2)',number=10**2,globals=globals())
    print('1# list',a)
    a = timeit('filter(lambda x: x<10**3,map(ord,map(chr,(randrange(0,10**2) for a in range(10**5)))))',number=10**2,globals=globals())
    print('2# filter',a)
    #print(list(filter(lambda x: x<10**3,map(ord,map(chr,(randrange(0,10**3) for a in range(10**2)))))))
