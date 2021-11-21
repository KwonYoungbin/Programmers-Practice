from collections import deque

def bfs(arr):
    points = []
    moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    for x in range(5):
        for y in range(5):
            if arr[x][y] == 'P':
                points.append([x, y])

    for point in points:
        q = deque([point])
        visited = [[False] * 5 for _ in range(5)]
        dist = [[0] * 5 for _ in range(5)]
        visited[point[0]][point[1]] = True

        while q:
            x, y = q.popleft()

            for move in moves:
                nx = x + move[0]
                ny = y + move[1]

                if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                    if arr[nx][ny] == 'P' and dist[x][y] <= 1:
                        return 0
                    if arr[nx][ny] == 'O':
                        q.append([nx, ny])
                        visited[nx][ny] = True
                        dist[nx][ny] = dist[x][y] + 1
    return 1


def solution(places):
    answer = []
    for place in places:
        answer.append(bfs(place))
    return answer