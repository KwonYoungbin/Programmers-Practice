def solution(m, n, puddles):
    answer = 0
    maps = [[1] * (m + 1) for _ in range(n + 1)]

    for x, y in puddles:
        maps[y][x] = 0

    for x in range(1, n + 1):
        for y in range(1, m + 1):
            if maps[x][y] == 1:
                left_y, up_x = y - 1, x - 1
                if left_y > 0 and up_x > 0:
                    maps[x][y] = (maps[x][left_y] + maps[up_x][y]) % 1000000007
                elif left_y > 0 and up_x == 0:
                    maps[x][y] = maps[x][left_y] % 1000000007
                elif left_y == 0 and up_x > 0:
                    maps[x][y] = maps[up_x][y] % 1000000007
    # print(*maps, sep='\n')
    return maps[-1][-1]