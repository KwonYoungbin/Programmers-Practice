def d2b(val):
    binary = []
    while val > 1:
        binary.append(val % 2)
        val //= 2
        if val == 1:
            binary.append(val)
    return binary[::-1]


def solution(n):
    cnt = d2b(n).count(1)

    while True:
        n += 1
        if d2b(n).count(1) == cnt:
            break

    return n

# def d2b(val):
#     binary = []
#     while val > 1:
#         binary.append(val % 2)
#         val //= 2
#         if val == 1:
#             binary.append(val)
#     return binary[::-1]

# def b2d(arr):
#     decimal = 0
#     for i in range(len(arr)):
#         decimal += arr[i] * (2**i)
#     return decimal

# def solution(n):
#     answer = 0
#     bi = d2b(n)

#     if 0 not in bi:
#         bi = [bi[0]] + [0] + bi[1:]
#     else:
#         for in range(1, len(bi)):


#     return answer