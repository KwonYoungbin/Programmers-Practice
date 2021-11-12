def solution(lottos, win_nums):
    answer = []
    zero_count = lottos.count(0)
    collect_count = 0

    for i in lottos:
        if i in win_nums:
            collect_count += 1

    if zero_count + collect_count >= 2:
        answer.append(7 - (zero_count + collect_count))
    else:
        answer.append(6)

    if collect_count >= 2:
        answer.append(7 - collect_count)
    else:
        answer.append(6)

    return answer