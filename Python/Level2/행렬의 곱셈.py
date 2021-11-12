def solution(arr1, arr2):
    answer = [[sum(a * b for a, b in zip(rowA, colB)) for colB in zip(*arr2)] for rowA in arr1]

    return answer