from collections import deque
moves = [(0,1), (0,-1), (1,0), (-1,0)]

def bfs(graph, start_x, start_y, end_x, end_y):
    q = deque([(0, start_x, start_y)])
    visited = [[False]*101 for _ in range(101)]
    visited[start_y][start_x] = True
    while q:
        dist, x, y = q.popleft()
        for move in moves:
            nx = x + move[0]
            ny = y + move[1]
            if 0 <= nx < 101 and 0 <= ny < 101 and graph[ny][nx] != 0 and not visited[ny][nx]:
                if nx == end_x and ny == end_y:
                    return (dist+1) // 2
                visited[ny][nx] = True
                q.append((dist+1, nx, ny))

def solution(rectangle, characterX, characterY, itemX, itemY):
    graph = [[0]*101 for _ in range(101)]
    for lb_x, lb_y, ru_x, ru_y in rectangle:
        lb_x *= 2
        lb_y *= 2
        ru_x *= 2
        ru_y *= 2
        for x in range(lb_x, ru_x+1):
            graph[lb_y][x] += 1
            graph[ru_y][x] += 1

        for y in range(lb_y, ru_y+1):
            graph[y][lb_x] += 1
            graph[y][ru_x] += 1

    for lb_x, lb_y, ru_x, ru_y in rectangle:
        lb_x *= 2
        lb_y *= 2
        ru_x *= 2
        ru_y *= 2
        for x in range(lb_x+1, ru_x):
            for y in range(lb_y+1, ru_y):
                graph[y][x] = 0
    return bfs(graph, characterX*2, characterY*2, itemX*2, itemY*2)