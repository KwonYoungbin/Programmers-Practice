def solution(rows, columns, queries):
    answer = []
    arr = [[0] * columns for _ in range(rows)]

    val = 1
    for row in range(rows):
        for col in range(columns):
            arr[row][col] = val
            val += 1

    for query in queries:
        x1, y1, x2, y2 = query

        moves = [(x1, y) for y in range(y1, y2 + 1)]
        moves += [(x, y2) for x in range(x1 + 1, x2 + 1)]
        moves += [(x2, y) for y in range(y2 - 1, y1 - 1, -1)]
        moves += [(x, y1) for x in range(x2 - 1, x1, -1)]

        val_list = []
        for x, y in moves:
            val_list.append(arr[x - 1][y - 1])
        val_list.insert(0, val_list.pop())

        for i in range(len(moves)):
            nx, ny = moves[i][0] - 1, moves[i][1] - 1
            arr[nx][ny] = val_list[i]

        answer.append(min(val_list))
    return answer