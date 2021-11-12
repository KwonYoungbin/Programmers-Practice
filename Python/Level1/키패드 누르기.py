def solution(numbers, hand):
    answer = ''

    phone = {1: (0, 0), 2: (0, 1), 3: (0, 2)
        , 4: (1, 0), 5: (1, 1), 6: (1, 2)
        , 7: (2, 0), 8: (2, 1), 9: (2, 2)
        , '*': (3, 0), 0: (3, 1), '#': (3, 2)}

    l_now, r_now = '*', '#'

    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer += 'L'
            l_now = i
        elif i == 3 or i == 6 or i == 9:
            answer += 'R'
            r_now = i
        else:
            l_len = abs(phone[l_now][0] - phone[i][0]) + abs(phone[l_now][1] - phone[i][1])
            r_len = abs(phone[r_now][0] - phone[i][0]) + abs(phone[r_now][1] - phone[i][1])
            if l_len == r_len:
                if hand == 'right':
                    answer += 'R'
                    r_now = i
                else:
                    answer += 'L'
                    l_now = i
            elif l_len < r_len:
                answer += 'L'
                l_now = i
            else:
                answer += 'R'
                r_now = i

    return answer