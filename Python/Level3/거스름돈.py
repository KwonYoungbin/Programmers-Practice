def solution(n, money):
    arr = [1] + [0] * n

    # 메모이제이션 기법
    for m in money:
        for i in range(m, n + 1):
            arr[i] += arr[i - m]
    return arr[-1]