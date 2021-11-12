def solution(n):
    max_val = sum(i for i in range(1, n + 1))
    answer = [0] * max_val
    x, y = 0, 1
    direction = 'D'  # D:Down , U:Up , R:Right
    idx = 0

    for i in range(1, max_val + 1):
        answer[idx] = i
        if direction == 'D':
            if idx + y >= max_val or answer[idx + y] != 0:
                direction = 'R'
                idx += 1
                x = 1
            else:
                idx += y
                y += 1
        elif direction == 'R':
            if idx + 1 >= max_val or answer[idx + x] != 0:
                direction = 'U'
                idx -= y
                x = 0
                y -= 1
            else:
                idx += 1
        elif direction == 'U':
            if answer[idx - y] != 0:
                direction = 'D'
                idx += y
                y += 1
            else:
                idx -= y
                y -= 1

    return answer