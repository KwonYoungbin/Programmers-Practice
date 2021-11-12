def solution(s):
    answer = ''
    s = s.split(' ')
    s = [s[i].capitalize() for i in range(len(s))]

    answer = ' '.join(s)

    return answer