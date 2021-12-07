from collections import defaultdict
import sys

sys.setrecursionlimit(10000000)

def loof(number, dic):
    if number not in dic:
        dic[number] = number + 1
        return number

    empty = loof(dic[number], dic)
    dic[number] = empty + 1
    return empty

def solution(k, room_number):
    answer = []
    dic = defaultdict()

    for number in room_number:
        if number not in dic:
            answer.append(number)
            dic[number] = number + 1
        else:
            answer.append(loof(number, dic))
    return answer