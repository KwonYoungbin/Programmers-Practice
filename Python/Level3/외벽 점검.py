from itertools import permutations

INF = int(1e9)

def solution(n, weak, dist):
    answer = INF
    length = len(weak)

    for i in range(length):
        weak.append(weak[i] + n)

    for i in range(length):
        for arr in permutations(dist, len(dist)):
            count = 0
            max_pos = weak[i] + arr[count]
            flag = True
            for j in range(i, i + length):
                if max_pos < weak[j]:
                    count += 1
                    if count >= len(dist):
                        flag = False
                        break
                    max_pos = weak[j] + arr[count]
            if flag:
                answer = min(answer, count + 1)

    return answer if answer != INF else -1