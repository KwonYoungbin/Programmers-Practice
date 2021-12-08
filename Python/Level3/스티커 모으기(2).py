# Dynamic Programming 문제!!!

def solution(sticker):
    if len(sticker) <= 2:
        return max(sticker)

    # case1. 첫번째 스티커를 뽑는 경우
    pick = [0] * (len(sticker) - 1)
    pick[0] = sticker[0]
    pick[1] = sticker[0]
    for i in range(2, len(sticker) - 1):
        pick[i] = max(pick[i - 1], pick[i - 2] + sticker[i])

    # case2. 첫번째 스티커를 안뽑는 경우
    non_pick = [0] * len(sticker)
    non_pick[1] = sticker[1]
    for i in range(2, len(sticker)):
        non_pick[i] = max(non_pick[i - 1], non_pick[i - 2] + sticker[i])

    return max(pick[-1], non_pick[-1])