def chk_arr(arr, row_min, row_max, col_min, col_max, value):
    cnt = 0
    for x in range(row_min, row_max):
        for y in range(col_min, col_max):
            if arr[x][y] == value:
                cnt += 1
    if cnt == 0:
        return 0
    elif cnt == (row_max - row_min) * (col_max - col_min):
        return 1

    val_cnt = 0
    row_mid = (row_min + row_max) // 2
    col_mid = (col_min + col_max) // 2

    val_cnt += chk_arr(arr, row_min, row_mid, col_min, col_mid, value)
    val_cnt += chk_arr(arr, row_mid, row_max, col_min, col_mid, value)
    val_cnt += chk_arr(arr, row_min, row_mid, col_mid, col_max, value)
    val_cnt += chk_arr(arr, row_mid, row_max, col_mid, col_max, value)

    return val_cnt

def solution(arr):
    answer = []
    n = len(arr)
    answer.append(chk_arr(arr, 0, n, 0, n, 0))
    answer.append(chk_arr(arr, 0, n, 0, n, 1))
    return answer