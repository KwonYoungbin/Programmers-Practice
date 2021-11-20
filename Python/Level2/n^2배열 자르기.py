def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        q, r = i//n, i%n
        if q >= r:
            answer.append(q+1)
        else:
            answer.append(r+1)
    return answer