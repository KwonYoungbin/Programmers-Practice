from collections import deque, defaultdict

def bfs(graph, start, parent, child, n):
    q = [start]
    visited = [False] * n

    while q:
        now = q.pop()

        if now in parent.keys() and not visited[parent[now]]:
            child[parent[now]] = now
            continue

        visited[now] = True
        for i in graph[now]:
            if not visited[i]:
                q.append(i)

        if now in child.keys():
            q.append(child[now])

    return True if False not in visited else False


def solution(n, path, order):
    graph = [[] for _ in range(n)]
    parent = defaultdict(int)
    child = defaultdict(int)
    for x, y in path:
        graph[x].append(y)
        graph[y].append(x)

    for f, s in order:
        parent[s] = f

    return bfs(graph, 0, parent, child, n)

# from collections import deque, defaultdict        # 효율성 낮은 버전

# def bfs(graph, start, avail, dic, n):
#     q = deque([start])
#     visited = [False] * n
#     route = []

#     while q:
#         flag = True
#         now = q.pop()

#         if avail[now]:
#             route.append(now)
#             visited[now] = True
#             if now in dic:
#                 avail[dic[now]] = True
#             for i in graph[now]:
#                 if i not in route:
#                     q.append(i)
#         else:
#             q.appendleft(now)

#         for val in q:
#             if avail[val]:
#                 flag = False
#                 break

#         if flag:
#             break

#     return True if len(route) == n else False

# def solution(n, path, order):
#     answer = True
#     graph = [[] for _ in range(n)]
#     avail = [True] * n
#     dic = defaultdict(int)
#     for x, y in path:
#         graph[x].append(y)
#         graph[y].append(x)

#     for f, s in order:
#         avail[s] = False
#         dic[f] = s

#     return bfs(graph, 0, avail, dic, n)