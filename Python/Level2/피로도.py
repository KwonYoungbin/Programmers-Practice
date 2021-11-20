from itertools import permutations

def solution(k, dungeons):
    answer = -1
    for arr in permutations(dungeons):
        temp = k
        cnt = 0
        for m, s in arr:
            if temp >= m:
                temp -= s
                cnt += 1
        answer = max(answer, cnt)
    return answer