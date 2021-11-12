def solution(N, stages):
    result = {}
    remain = len(stages)

    for i in range(1, N + 1):
        if remain != 0:
            count = stages.count(i)
            result[i] = count / remain
            remain -= count
        else:
            result[i] = 0

    return sorted(result, key=lambda x: result[x], reverse=True)