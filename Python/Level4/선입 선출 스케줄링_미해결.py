def solution(n, cores):
    answer = 0
    if n <= len(cores):
        return n
    n -= len(cores)

    left = 1
    right = max(cores) * n
    while left < right:
        mid = (left + right) // 2

        counter = 0
        for c in cores:
            counter += mid // c

        if counter >= n:
            right = mid
        else:
            left = mid + 1

    for c in cores:
        n -= (right - 1) // c

    for idx, c in enumerate(cores):
        if right % c == 0:
            n -= 1
            if n == 0:
                answer = idx + 1
                break

    return answer

# from collections import deque
#
# def solution(n, cores):                       # 효율성 테스트5만 통과 못한 버전
#     answer = 0
#     if n <= len(cores):
#         return n
#
#     arr = deque([[] for _ in range(max(cores))])
#     n -= len(cores)
#
#     for i, val in enumerate(cores):
#         arr[val - 1].append(i)
#
#     while n > 0:
#         now = arr.popleft()
#         arr.append([])
#         if len(now) != 0:
#             n -= len(now)
#             for idx in now:
#                 arr[cores[idx] - 1].append(idx)
#
#             if n <= 0:
#                 now.sort()
#                 answer = now[n - 1] + 1
#
#     return answer