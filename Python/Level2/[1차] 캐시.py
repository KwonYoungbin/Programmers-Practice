from collections import deque


def solution(cacheSize, cities):
    answer = 0
    stack = deque()

    if cacheSize == 0:
        return 5 * len(cities)

    for city in cities:
        city = city.lower()
        if city in stack:
            answer += 1
            stack.remove(city)
        else:
            answer += 5
            if len(stack) >= cacheSize:
                stack.popleft()
        stack.append(city)
    return answer