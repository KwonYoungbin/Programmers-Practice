from collections import deque

def solution(progresses, speeds):
    answer = []
    speeds = deque(speeds)

    while progresses:
        count = 0
        progresses = deque([x + y for x, y in zip(progresses, speeds)])

        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            count += 1

        if count != 0:
            answer.append(count)

    return answer