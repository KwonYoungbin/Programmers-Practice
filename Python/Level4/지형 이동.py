from collections import deque, defaultdict
import heapq


def solution(land, height):
    answer = 0
    n = len(land)
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False] * n for _ in range(n)]
    q = [[0, 0, 0]]

    while q:
        v, x, y = heapq.heappop(q)
        if visited[x][y]:
            continue
        visited[x][y] = True
        answer += v
        for move in moves:
            nx = x + move[0]
            ny = y + move[1]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if abs(land[nx][ny] - land[x][y]) > height:
                    heapq.heappush(q, [abs(land[nx][ny] - land[x][y]), nx, ny])
                else:
                    heapq.heappush(q, [0, nx, ny])

    return answer

# from collections import deque, defaultdict                    # 내가 직접 구현한 코드 (틀림)

# def solution(land, height):
#     answer = 0
#     n = len(land)
#     arr = [[0] * n for _ in range(n)]
#     moves = [(0,1), (1,0), (0,-1), (-1,0)]

#     val = 1
#     for x in range(n):
#         for y in range(n):
#             if arr[x][y] != 0:
#                 continue
#             arr[x][y] = val

#             q = deque([(x, y)])
#             while q:
#                 now_x, now_y = q.popleft()
#                 for move in moves:
#                     nx = now_x + move[0]
#                     ny = now_y + move[1]
#                     if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0 and abs(land[nx][ny] - land[now_x][now_y]) <= height:
#                         q.append((nx, ny))
#                         arr[nx][ny] = val
#             val += 1

#     temp = set()
#     for x in range(n):
#         for y in range(n):
#             now = arr[x][y]
#             for move in moves:
#                 nx = x + move[0]
#                 ny = y + move[1]
#                 if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != now:
#                     if (abs(land[nx][ny] - land[x][y]), arr[nx][ny], now) not in temp:
#                         temp.add((abs(land[nx][ny] - land[x][y]), now, arr[nx][ny]))
#     temp = deque(sorted(temp, key=lambda x:x[0]))

#     chk_list = set()
#     while len(chk_list) < val-1:
#         value, f, t = temp.popleft()
#         if f in chk_list and t in chk_list:
#             continue

#         answer += value
#         chk_list.add(f)
#         chk_list.add(t)

#     return answer