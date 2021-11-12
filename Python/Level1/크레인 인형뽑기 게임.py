def solution(board, moves):
    answer = 0
    size = len(board)
    pool = []

    for i in moves:
        for j in range(size):
            if board[j][i - 1] != 0:
                pool.append(board[j][i - 1])
                board[j][i - 1] = 0
                if len(pool) >= 2 and pool[-1] == pool[-2]:
                    pool = pool[:-2]
                    answer += 2
                break

    return answer