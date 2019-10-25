# Binary search in O(log n)
def binary_search(A,x):
    n = len(A)
    beg = 0
    end = n - 1
    result = -1
    while beg <= end:
        mid = (beg + end) // 2
        if A[mid] <= x:
            beg = mid + 1
            result = mid
        else:
            end = mid - 1
    return result


def boards(A,k):
    n = len(A)
    beg = 1
    end = n
    result = -1
    while beg <= end:
        mid = (beg+end) // 2
        if check(A,mid) <= k:
            end = mid - 1
            result = mid
        else:
            beg =  mid + 1
        print('mid', mid)
    print('result', result)
    return result

# Greedily check in O(n)
def check(A,k):
    n = len(A)
    boards = 0
    last = -1
    for i in range(n):
        if A[i] == 1 and last < i:
            boards += 1
            last = i + k - 1
    print('boads', boards)
    return boards


if __name__ == '__main__':
    A = [i for i in range(100)]
    x = 3
    a = boards(A,x)
