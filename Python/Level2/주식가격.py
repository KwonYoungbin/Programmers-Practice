from collections import deque


def solution(prices):
    answer = []
    prices = deque(prices)

    while prices:
        now = prices.popleft()
        if not prices:
            answer.append(0)
            break

        count = 0
        for i in prices:
            count += 1
            if i < now:
                break
        answer.append(count)

    return answer