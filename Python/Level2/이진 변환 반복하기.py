def lenToBin(val):
    result = ''
    while val > 0:
        result += str(val % 2)
        val //= 2
    return result[::-1]


def solution(s):
    answer = [0, 0]

    while s != '1':
        zero_cnt, one_cnt = s.count('0'), s.count('1')
        answer[0] += 1
        answer[1] += zero_cnt
        s = lenToBin(one_cnt)

    return answer