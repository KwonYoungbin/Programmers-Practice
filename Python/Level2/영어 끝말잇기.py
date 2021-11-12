def solution(n, words):
    answer = [0,0]
    stack = []
    for i in range(len(words)):
        if stack and (words[i] in stack or stack[-1][-1] != words[i][0]):
            answer = [(i%n)+1, (i//n)+1]
            break
        stack.append(words[i])
    return answer