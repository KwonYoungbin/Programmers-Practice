def solution(n):
    arr = [0, 1]
    for i in range(2, n + 1):
        arr.append(arr[i - 2] + arr[i - 1])
    return arr[-1] % 1234567

# from collections import deque

# def solution(n):
#     answer = 0
#     q = deque([0,1])

#     for i in range(n-1):
#         q.append(q[0]+q[1])
#         q.popleft()

#     answer = q[-1] % 1234567
#     return answer