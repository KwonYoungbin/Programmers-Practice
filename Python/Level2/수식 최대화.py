from itertools import permutations


def operation(num1, num2, op):
    if op == '+':
        return str(int(num1) + int(num2))
    if op == '-':
        return str(int(num1) - int(num2))
    if op == '*':
        return str(int(num1) * int(num2))


def solution(expression):
    s = []
    arr = []
    result = []

    if '-' in expression:
        s.append('-')
    if '*' in expression:
        s.append('*')
    if '+' in expression:
        s.append('+')
    s = list(permutations(s, len(s)))

    now = ''
    for i in expression:
        if i.isdigit():
            now += i
        else:
            arr.append(now)
            arr.append(i)
            now = ''
    arr.append(now)

    for i in s:
        cp = arr.copy()
        for j in i:
            stack = []
            while len(cp) != 0:
                temp = cp.pop(0)
                if temp == j:
                    stack.append(operation(stack.pop(), cp.pop(0), j))
                else:
                    stack.append(temp)
            cp = stack
        result.append(abs(int(cp[0])))

    return max(result)