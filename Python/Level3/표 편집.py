def solution(n, k, cmd):
    answer = ['O'] * n
    linkedlist = {i: [i - 1, i + 1] for i in range(n)}
    stack = []

    for c in cmd:
        c = c.split()
        if c[0] == 'D':
            for _ in range(int(c[1])):
                k = linkedlist[k][1]
        elif c[0] == 'U':
            for _ in range(int(c[1])):
                k = linkedlist[k][0]
        elif c[0] == 'C':
            prev, nxt = linkedlist[k]
            stack.append([prev, k, nxt])
            answer[k] = 'X'
            if nxt == n:
                k = linkedlist[k][0]
            else:
                k = linkedlist[k][1]

            if prev == -1:
                linkedlist[nxt][0] = prev
            elif nxt == n:
                linkedlist[prev][1] = nxt
            else:
                linkedlist[prev][1] = nxt
                linkedlist[nxt][0] = prev
        elif c[0] == 'Z':
            prev, now, nxt = stack.pop()
            answer[now] = 'O'

            if prev == -1:
                linkedlist[nxt][0] = now
            elif nxt == n:
                linkedlist[prev][1] = now
            else:
                linkedlist[prev][1] = now
                linkedlist[nxt][0] = now
    return ''.join(answer)