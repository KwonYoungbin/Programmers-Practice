def solution(a):
    if len(a) < 3:
        return len(a)

    chk = [0] * len(a)
    chk[0] = 1
    chk[-1] = 1

    left = a[0]
    right = a[-1]

    for i in range(1, len(a)):
        if a[i] < left:
            left = a[i]
            chk[i] = 1
        if a[-i - 1] < right:
            right = a[-i - 1]
            chk[-i - 1] = 1
    return sum(chk)