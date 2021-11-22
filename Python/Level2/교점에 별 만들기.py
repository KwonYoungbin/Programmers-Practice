INF = int(1e9)

# 테스트 케이스 시간 초과 있음.
def solution(line):
    crossed = []
    minx, miny, maxx, maxy = INF, INF, -INF, -INF

    for i in range(len(line) - 1):
        a, b, e = line[i]
        for j in range(i + 1, len(line)):
            c, d, f = line[j]
            bottom = a * d - b * c
            xtop = b * f - e * d
            ytop = e * c - a * f
            if bottom != 0 and xtop % bottom == 0 and ytop % bottom == 0:
                nx = xtop // bottom
                ny = ytop // bottom
                minx, miny = min(minx, nx), min(miny, ny)
                maxx, maxy = max(maxx, nx), max(maxy, ny)
                crossed.append((nx, ny))

    answer = [['.'] * (maxx - minx + 1) for _ in range(maxy - miny + 1)]

    for x, y in crossed:
        answer[maxy - y][x - minx] = '*'

    return [''.join(result) for result in answer]