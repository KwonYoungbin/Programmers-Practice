def chk(m, n, arr):
    result = 0
    while True:
        remove_pos = set()
        for col in range(m - 1):
            for row in range(n - 1):
                if arr[row][col] == arr[row][col + 1] == arr[row + 1][col] == arr[row + 1][col + 1] != 'X':
                    remove_pos.add((row, col))
                    remove_pos.add((row, col + 1))
                    remove_pos.add((row + 1, col))
                    remove_pos.add((row + 1, col + 1))

        if len(remove_pos) == 0:
            break
        result += len(remove_pos)

        for nx, ny in remove_pos:
            arr[nx][ny] = 'X'

        for i in range(len(arr)):
            arr[i] = ['X'] * arr[i].count('X') + [val for val in arr[i] if val != 'X']

    return result


def solution(m, n, board):
    answer = 0
    board = list(map(list, zip(*board)))
    answer = chk(m, n, board)
    return answer