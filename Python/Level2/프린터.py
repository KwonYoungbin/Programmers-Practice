from collections import deque


def solution(priorities, location):
    answer = 0
    q = deque([(x, y) for x, y in enumerate(priorities)])

    while True:
        cur = q.popleft()
        if any(cur[1] < temp[1] for temp in q):
            q.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

# from collections import deque

# def solution(priorities, location):
#     answer = 0
#     order = []
#     idx = 0

#     while len(order) < len(priorities):
#         if priorities[idx] == max(priorities):
#             order.append(idx)
#             priorities[idx] = 0
#         idx += 1
#         idx %= len(priorities)

#     answer = order.index(location)+1
#     return answer