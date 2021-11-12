def solution(dartResult):
    dartResult = dartResult.replace('10', 'x')

    arr = []
    now = 0
    for i in dartResult:
        if i.isdigit() or i == 'x':
            now = (10 if i == 'x' else int(i))
        elif i == 'S':
            arr.append(now)
            now = 0
        elif i == 'D':
            arr.append(now ** 2)
            now = 0
        elif i == 'T':
            arr.append(now ** 3)
            now = 0
        elif i == '*':
            if len(arr) == 1:
                arr[0] *= 2
            else:
                arr[-2] *= 2
                arr[-1] *= 2
        elif i == '#':
            arr[-1] *= -1

    return sum(arr)