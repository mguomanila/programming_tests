from math import sqrt, pow

def fibonnaci(n):
    a = (1 + sqrt(5))/2
    b = (1 - sqrt(5))/2
    c = sqrt(5)
    return int((pow(a,n)-pow(b,n))/c)
