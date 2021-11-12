def cal(bit):
    if bit.count(0) == 0:
        bit = bit[:-1] + [0] + [bit[-1]]
    else:
        bit = list(map(int, ''.join(map(str, bit)).replace('10', '01', 1)))

    result = 0
    for i in range(len(bit)):
        result += bit[i] * (2 ** i)

    return result


def d2b(val):
    result = []
    while val > 0:
        result.append(val % 2)
        val //= 2

    return result


def solution(numbers):
    answer = []
    for number in numbers:
        if number % 2 == 0:
            answer.append(number + 1)
        else:
            bi = d2b(number)
            answer.append(cal(bi))

    return answer