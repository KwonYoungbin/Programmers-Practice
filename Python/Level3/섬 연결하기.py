from collections import deque

def bfs(start, graph):
    q = deque([start])
    visited = [False] * len(graph)
    visited[start] = True
    route = [start]
    while q:
        now = q.popleft()

        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                route.append(i)
    return route

def solution(n, costs):
    answer = 0
    costs = deque(sorted(costs, key=lambda x: x[2], reverse=True))

    for _ in range(len(costs)):
        now = costs.popleft()
        graph = [[] for _ in range(n)]
        for s, e, w in costs:
            graph[s].append(e)
            graph[e].append(s)
        route = bfs(0, graph)
        if len(route) != n:
            costs.append(now)

    for s, e, w in costs:
        answer += w

    return answer