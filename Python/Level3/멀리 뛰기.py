def solution(n):
    result = [1, 2]

    for i in range(2, n):
        result.append((result[i - 2] + result[i - 1]) % 1234567)

    return result[n - 1]