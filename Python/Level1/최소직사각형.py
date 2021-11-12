def solution(sizes):
    min_arr = []
    max_arr = []

    for x, y in sizes:
        min_arr.append(min(x, y))
        max_arr.append(max(x, y))

    return max(min_arr) * max(max_arr)