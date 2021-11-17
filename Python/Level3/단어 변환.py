from collections import deque

answer = 0

def bfs(start, target, visited, words):
    global answer
    q = deque([(start, 0)])

    while q:
        now, cnt = q.popleft()
        if now == target:
            answer = cnt
            break

        for i in range(len(words)):
            dif_cnt = 0
            for j in range(len(now)):
                if now[j] != words[i][j]:
                    dif_cnt += 1

            if dif_cnt == 1 and not visited[i]:
                visited[i] = True
                q.append((words[i], cnt + 1))


def solution(begin, target, words):
    global answer
    visited = [False] * len(words)
    bfs(begin, target, visited, words)
    return answer