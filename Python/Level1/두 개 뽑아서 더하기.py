from itertools import combinations


def solution(numbers):
    answer = list(set(list(map(sum, combinations(numbers, 2)))))

    return sorted(answer)