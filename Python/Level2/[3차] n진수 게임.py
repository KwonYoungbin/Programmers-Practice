def cvt(val, n):
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    result = []
    while val > 0:
        result.append(number[val % n])
        val //= n
    return result[::-1]


def solution(n, t, m, p):
    arr = [0]
    num = 0

    while True:
        arr += cvt(num, n)
        if len(arr) >= t * m:
            break
        num += 1

    return ''.join(map(str, [arr[i] for i in range(p - 1, t * m, m)]))