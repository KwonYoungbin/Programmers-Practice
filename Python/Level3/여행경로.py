def solution(tickets):
    answer = []
    dic = {}

    for start, end in tickets:
        if start in dic:
            dic[start].append(end)
        else:
            dic[start] = [end]

    for i in dic.keys():
        dic[i].sort(reverse=True)

    q = ['ICN']
    while q:
        now = q[-1]
        if now in dic and dic[now]:
            q.append(dic[now].pop())
        else:
            answer.append(q.pop())

    return answer[::-1]