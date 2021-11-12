from collections import deque


def chk(arr):
    left = ['[', '(', '{']
    stack = []
    for i in arr:
        if i in left:
            stack.append(i)
        else:
            if stack:
                if (i == ']' and stack[-1] == '['):
                    stack.pop()
                elif (i == ')' and stack[-1] == '('):
                    stack.pop()
                elif (i == '}' and stack[-1] == '{'):
                    stack.pop()
                else:
                    return 0
            else:
                return 0
    return 1 if not stack else 0


def solution(s):
    answer = 0
    s = deque(s)

    for i in range(len(s)):
        answer += chk(s)
        s.append(s.popleft())

    return answer