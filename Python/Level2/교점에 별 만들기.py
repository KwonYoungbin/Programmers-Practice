def solution(line):
    x_list, y_list = [], []

    for i in range(len(line) - 1):
        a, b, e = line[i]
        for j in range(i + 1, len(line)):
            c, d, f = line[j]
            bottom = a * d - b * c
            if bottom == 0:
                continue

            xtop = b * f - e * d
            ytop = e * c - a * f
            if xtop % bottom == 0 and ytop % bottom == 0:
                nx = xtop // bottom
                ny = ytop // bottom
                x_list.append(int(nx))
                y_list.append(int(ny))

    min_x, max_x = min(x_list), max(x_list)
    min_y, max_y = min(y_list), max(y_list)
    x_size = max_x - min_x + 1
    y_size = max_y - min_y + 1

    answer = [['.'] * x_size for _ in range(y_size)]

    for x, y in zip(x_list, y_list):
        answer[max_y - y][x - min_x] = '*'

    return [''.join(result) for result in answer]