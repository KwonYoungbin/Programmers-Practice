def solution(n):
    arr = [0] * (n+1)
    arr[0] = 1
    sub = 0
    for i in range(2, n+1, 2):
        arr[i] = (arr[i-2] * 3 + sub * 2) % 1000000007
        sub += arr[i-2]
    return arr[n]