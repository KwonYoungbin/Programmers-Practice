import math

def solution(n, k):
    answer = []
    arr = list(range(1, n + 1))

    while n != 0:
        fact = math.factorial(n - 1)
        idx = (k - 1) // fact
        k = k % fact
        answer.append(arr.pop(idx))
        n -= 1

    return answer