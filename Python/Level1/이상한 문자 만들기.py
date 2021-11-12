def solution(s):
    answer = ''
    idx = 0
    s = s.lower()
    for i in s:
        if i == ' ':
            idx = 0
            answer += ' '
            continue

        if idx % 2 == 0:
            answer += i.upper()
        else:
            answer += i
        idx += 1
    return answer