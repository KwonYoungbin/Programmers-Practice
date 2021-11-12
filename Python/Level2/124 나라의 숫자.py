def solution(n):
    answer = ''
    while n > 0:
        mod = n%3
        answer += str(mod) if mod != 0 else '4'
        n = (n-1) // 3
    return answer[::-1]