def solution(s, n):
    answer = ''
    lower = 'abcdefghijklmnopqrstuvwxyz'
    length = len(lower)

    for i in s:
        if i.islower():
            answer += lower[(lower.index(i) + n) % length]
        elif i.isupper():
            upper = lower.upper()
            answer += upper[(upper.index(i) + n) % length]
        else:
            answer += ' '
    return answer