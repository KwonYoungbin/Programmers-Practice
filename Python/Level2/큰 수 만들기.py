def solution(number, k):
    stack = []

    for i in number:
        if not stack or stack[-1] >= i:
            stack.append(i)
        else:
            if k > 0:
                while True:
                    stack.pop()
                    k -= 1
                    if not stack or stack[-1] >= i or k < 1:
                        break
            stack.append(i)
    return ''.join(stack) if k == 0 else ''.join(stack[:-k])