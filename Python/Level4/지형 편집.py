def solution(land, P, Q):
    heights = []
    for l in land:
        heights += l
    heights.sort()

    length = len(heights)
    answer = sum(heights) * Q  # 0층에 맞출 때.
    cost = (sum(heights) - heights[0] * length) * Q  # 가장 낮은 층 높이에 맞춰 블록을 만드는 경우.
    answer = min(answer, cost)

    for i in range(1, length):
        if heights[i] != heights[i - 1]:
            cost += (P * i * (heights[i] - heights[i - 1])) - (Q * (length - i) * (heights[i] - heights[i - 1]))
            answer = min(answer, cost)      # i번째를 기준으로 왼쪽은 높이고, 오른쪽은 낮춰줌

    return answer