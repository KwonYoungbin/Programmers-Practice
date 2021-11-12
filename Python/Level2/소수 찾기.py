from itertools import permutations


def chk_prime(value):
    if value <= 1 or (value % 2 == 0 and value != 2):
        return False
    elif value == 2:
        return True
    else:
        for i in range(3, int(value ** (1 / 2)) + 1):
            if value % i == 0:
                return False
        return True


def solution(numbers):
    length = len(numbers)
    arr = []

    for i in range(1, length + 1):

        for j in set(list(map(''.join, permutations(numbers, i)))):
            if chk_prime(int(j)):
                arr.append(int(j))

    return len(set(arr))

# def find_s(num):
#     for i in range(2, int(num**(1/2))+1):
#         if num % i == 0:
#             return False
#     return True


# def solution(numbers):
#     answer = 0
#     arr = []

#     for i in range(1, len(numbers)+1):
#         temp = list(map(''.join, permutations(numbers, i)))

#         for j in temp:
#             if find_s(int(j)) and int(j) not in (0,1):
#                 arr.append(int(j))

#     answer = len(set(arr))

#     return answer