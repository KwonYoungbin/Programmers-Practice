def solution(board):
    for row in range(1,len(board)):
        for col in range(1, len(board[0])):
            if board[row][col] == 1:
                board[row][col] = min(board[row-1][col], board[row][col-1], board[row-1][col-1]) + 1

    return max(max(i) for i in board)**2