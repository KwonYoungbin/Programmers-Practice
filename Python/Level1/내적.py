def solution(a, b):
    answer = sum([x*y for x,y in zip(a,b)])
    return answer