def solution(n, m):
    x, y = max(n, m), min(n, m)
    mod = x % y

    while mod > 0:
        x = y
        y = mod
        mod = x % y

    return [y, (n * m) // y]