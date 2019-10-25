def gcd(a,b):
    if not a % b:
        return b
    else:
        return gcd(b, a%b)


def solution(N, M):
    # write your code in Python 3.6
    count = 0
    while not gcd(N,M):
        count += 1
    return count


if __name__ == '__main__':
    a = solution(10,4)
