from collections import deque

# 효율성 통과 X   / info <= 50000 , query <= 100000
def solution(info, query):
    answer = []

    cond = deque()
    for q in query:
        condition = q.split(' and ')
        condition += condition.pop().split()
        cond.append(condition)

    datas = []
    for i in info:
        datas.append(i.split())

    while cond:
        lan, pos, y, food, score = cond.popleft()
        cnt = 0
        for data in datas:
            c_l, c_p, c_y, c_f, c_s = data
            if lan != '-' and lan != c_l:
                continue
            if pos != '-' and pos != c_p:
                continue
            if y != '-' and y != c_y:
                continue
            if food != '-' and food != c_f:
                continue
            if int(c_s) >= int(score):
                cnt += 1
        answer.append(cnt)

    return answer