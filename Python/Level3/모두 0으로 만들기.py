import sys
sys.setrecursionlimit(300000)
answer = 0

def dfs(graph, start, visited, a):
    global answer
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            a[start] += dfs(graph, i, visited, a)
    answer += abs(a[start])

    return a[start]

def solution(a, edges):
    global answer

    if sum(a) != 0:
        return -1
    elif a.count(0) == len(a):
        return 0

    graph = [[] for _ in range(len(a))]
    visited = [False] * len(a)
    for s, e in edges:
        graph[s].append(e)
        graph[e].append(s)

    dfs(graph, 0, visited, a)
    return answer