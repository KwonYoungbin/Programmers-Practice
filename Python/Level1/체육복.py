def solution(n, lost, reserve):
    both = set(lost) & set(reserve)
    lost = set(lost) - both
    reserve = set(reserve) - both

    for i in reserve:
        if i - 1 in lost:
            lost.remove(i - 1)
        elif i + 1 in lost:
            lost.remove(i + 1)

    return n - len(lost)