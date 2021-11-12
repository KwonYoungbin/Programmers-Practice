from collections import deque


def gcd(a, b):
    x, y = max(a, b), min(a, b)
    mod = x % y

    while mod > 0:
        x = y
        y = mod
        mod = x % y
    return y


def solution(arr):
    arr = deque(arr)

    while len(arr) > 1:
        a, b = arr.popleft(), arr.popleft()
        arr.append((a * b) // gcd(a, b))

    return arr[0]