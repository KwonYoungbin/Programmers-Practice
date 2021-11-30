INF = int(1e9)

def solution(n, s, a, b, fares):
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        graph[i][i] = 0

    for start, end, fee in fares:
        graph[start][end] = fee
        graph[end][start] = fee

    for k in range(1, n + 1):
        for x in range(1, n + 1):
            for y in range(1, n + 1):
                if graph[x][y] > graph[x][k] + graph[k][y]:
                    graph[x][y] = graph[x][k] + graph[k][y]

    answer = INF
    for i in range(1, n + 1):
        answer = min(answer, graph[s][i] + graph[i][a] + graph[i][b])
    return answer
