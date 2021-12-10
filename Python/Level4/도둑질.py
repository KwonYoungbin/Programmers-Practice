def solution(money):
    # case 1: 첫 집을 털 때.
    pick1 = [0] * (len(money) - 1)
    pick1[0] = money[0]
    pick1[1] = money[0]

    for i in range(2, len(money) - 1):
        pick1[i] = max(pick1[i - 1], pick1[i - 2] + money[i])

    # case 2: 첫 집은 안 털 때.
    non_pick1 = [0] * len(money)
    non_pick1[1] = money[1]

    for i in range(2, len(money)):
        non_pick1[i] = max(non_pick1[i - 1], non_pick1[i - 2] + money[i])

    return max(pick1[-1], non_pick1[-1])