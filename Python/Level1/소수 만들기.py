from itertools import combinations


def prime(val):
    if val % 2 == 0:
        return 0
    else:
        for i in range(3, int(val ** (1 / 2)) + 1, 2):
            if val % i == 0:
                return 0
        return 1


def solution(nums):
    answer = 0
    sum_arr = list(map(sum, combinations(nums, 3)))
    for i in sum_arr:
        answer += prime(i)

    return answer

# from itertools import combinations

# def chk_prime(v):
#     if v % 2 == 0:
#         return 0
#     else:
#         for i in range(3, int(v**(1/2))+1, 2):
#             if v % i == 0:
#                 return 0
#         return 1

# def solution(nums):
#     answer = 0
#     comb = combinations(nums, 3)

#     for i in comb:
#         answer += chk_prime(sum(i))

#     return answer