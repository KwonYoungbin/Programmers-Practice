def solution(dirs):
    x, y = 0, 0
    arr = set()

    for move in dirs:
        if move == 'U' and y < 5:
            arr.add(((x, y), (x, y + 1)))
            y += 1
        elif move == 'D' and y > -5:
            arr.add(((x, y - 1), (x, y)))
            y -= 1
        elif move == 'R' and x < 5:
            arr.add(((x, y), (x + 1, y)))
            x += 1
        elif move == 'L' and x > -5:
            arr.add(((x - 1, y), (x, y)))
            x -= 1
    return len(arr)