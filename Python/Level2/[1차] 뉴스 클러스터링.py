import math


def solution(str1, str2):
    answer = 0
    str1 = str1.upper()
    str2 = str2.upper()
    arr1 = []
    arr2 = []

    for i in range(len(str1) - 1):
        if str1[i:i + 2].isalpha():
            arr1.append(str1[i:i + 2])

    for i in range(len(str2) - 1):
        if str2[i:i + 2].isalpha():
            arr2.append(str2[i:i + 2])

    inter = set(arr1) & set(arr2)
    uni = set(arr1) | set(arr2)

    if len(uni) == 0:
        return 65536
    else:
        _and = sum([min(arr1.count(i), arr2.count(i)) for i in inter])
        _or = sum([max(arr1.count(i), arr2.count(i)) for i in uni])
        answer = (_and / _or) * 65536
    return math.floor(answer)