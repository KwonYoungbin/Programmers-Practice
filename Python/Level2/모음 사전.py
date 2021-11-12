from itertools import product


def solution(word):
    answer = 0
    arr = []
    arr = list(map(''.join, list(map(list, product('AEIOU', repeat=1)))))
    arr2 = list(map(''.join, list(map(list, product('AEIOU', repeat=2)))))
    arr3 = list(map(''.join, list(map(list, product('AEIOU', repeat=3)))))
    arr4 = list(map(''.join, list(map(list, product('AEIOU', repeat=4)))))
    arr5 = list(map(''.join, list(map(list, product('AEIOU', repeat=5)))))
    arr += arr2 + arr3 + arr4 + arr5
    arr.sort()

    return arr.index(word) + 1