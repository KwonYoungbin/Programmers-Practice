from collections import deque

# 이해하는데 어려움이 있었음...

def solution(s):
    answer = []
    for string in s:
        cnt = 0
        stack = []
        for a in string:
            if len(stack) >= 2 and stack[-2:] == ['1', '1'] and a == '0':
                cnt += 1
                stack.pop()
                stack.pop()
            else:
                stack.append(a)

        if cnt == 0:
            answer.append(string)
        else:
            q = deque()
            while stack:
                if stack[-1] == '1':
                    q.append(stack.pop())
                else:
                    break
            while cnt > 0:
                q.appendleft('0')
                q.appendleft('1')
                q.appendleft('1')
                cnt -= 1
            while stack:
                q.appendleft(stack.pop())
            answer.append(''.join(q))

    return answer