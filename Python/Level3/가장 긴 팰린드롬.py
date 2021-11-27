def chk(string):
    # case 1 (짝수인 경우)
    case1 = 1
    for pivot in range(0, len(string) - 1):
        if string[pivot] == string[pivot + 1]:
            cnt = 2
            left = pivot - 1
            right = pivot + 2
            while left >= 0 and right < len(string):
                if string[left] == string[right]:
                    cnt += 2
                    left -= 1
                    right += 1
                else:
                    break
            case1 = max(case1, cnt)

    # case 2 (홀수인 경우)
    case2 = 1
    for pivot in range(1, len(string) - 1):
        left = pivot - 1
        right = pivot + 1
        cnt = 1
        while left >= 0 and right < len(string):
            if string[left] == string[right]:
                cnt += 2
                left -= 1
                right += 1
            else:
                break
        case2 = max(case2, cnt)

    return max(case1, case2)


def solution(s):
    return chk(s)