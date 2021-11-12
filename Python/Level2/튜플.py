def solution(s):
    answer = []
    s = s[1:-1]
    list_set = []

    temp = []
    now = ''
    for i in s:
        if i.isdigit():
            now += i
        elif i == ',' and now != '':
            temp.append(now)
            now = ''
        elif i == '}' and now != '':
            temp.append(now)
            now = ''
            list_set.append(temp)
            temp = []
    list_set = sorted(list_set, key=len)

    for i in list_set:
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))

    return answer