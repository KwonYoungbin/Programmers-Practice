# 카탈란 수

def solution(n):
    answer = 0
    result = [1,1,2,5]
    for i in range(4, n+1):
        temp = 0
        for j in range(i):
            temp += result[j]*result[i-j-1]
        result.append(temp)
    return result[n]