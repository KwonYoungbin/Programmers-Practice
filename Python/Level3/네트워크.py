from collections import deque

def bfs(arr, start, visited, dic):
    q = deque([start])
    visited[start] = True
    dic[start] = [start]

    while q:
        now = q.popleft()
        for i in arr[now]:
            if not visited[i]:
                visited[i] = True
                dic[start].append(i)
                q.append(i)

def solution(n, computers):
    visited = [False] * n
    arr = []
    dic = {}

    for i in range(len(computers)):
        temp = []
        for j in range(len(computers[i])):
            if i != j and computers[i][j] == 1:
                temp.append(j)
        arr.append(temp)

    for i in range(n):
        if not visited[i]:
            bfs(arr, i, visited, dic)

    return len(dic)