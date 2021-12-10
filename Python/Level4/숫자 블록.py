def get_divisor(val):
    if val == 1:
        return 0
    for i in range(2, int(val**(1/2))+1):
        if val % i == 0 and val // i <= 10000000:   # 1,000,000,000개의 블록 중 10,000,000번 블록까지만 설정되어있기때문
            return val//i
    return 1

def solution(begin, end):
    answer = []
    for i in range(begin, end+1):
        answer.append(get_divisor(i))
    return answer

# import math

# def get_divisor(val):
#     if val < 2:
#         return 0
#     for i in range(2, int(math.sqrt(val))+1):
#         if val % i == 0:
#             return val//i
#     return 1

# def solution(begin, end):
#     answer = []
#     for i in range(begin, end+1):
#         if i < 2:
#             answer.append(0)
#             continue
#         else:
#             for j in range(2, int(math.sqrt(i))+1):
#                 if i % j == 0 and i // j <= 10000000:
#                     answer.append(i//j)
#                     break
#             else:
#                 answer.append(1)
#     return answer