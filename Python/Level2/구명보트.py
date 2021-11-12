from collections import deque


def solution(people, limit):
    answer = 0
    people = deque(sorted(people))

    while len(people) > 1:
        left = people.popleft()
        right = people.pop()
        if left + right > limit:
            people.appendleft(left)
        answer += 1

    return answer if not people else answer + 1