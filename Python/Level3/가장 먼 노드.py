import heapq

INF = int(1e9)

def dijkstra(start, graph, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))


def solution(n, edge):
    answer = 0
    distance = [INF] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for start, end in edge:
        graph[start].append(end)
        graph[end].append(start)

    dijkstra(1, graph, distance)

    return distance.count(max(distance[1:]))