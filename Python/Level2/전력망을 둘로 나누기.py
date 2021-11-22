from collections import deque

def bfs(start, graph, n):
    count = 1
    q = deque([start])
    visited = [False] * (n + 1)
    visited[start] = True

    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                count += 1

    return count

def solution(n, wires):
    answer = n
    wires = deque(wires)

    for _ in range(n - 1):
        a, b = wires.popleft()
        con = [[] for _ in range(n + 1)]

        for f, t in wires:
            con[f].append(t)
            con[t].append(f)

        answer = min(answer, abs(bfs(a, con, n) - bfs(b, con, n)))
        wires.append([a, b])

    return answer