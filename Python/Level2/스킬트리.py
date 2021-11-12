def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        answer += 1
        stack = []
        for i in range(len(skill)):
            if skill[i] in tree:
                idx = tree.index(skill[i])
                if stack and (stack[-1] == -1 or stack[-1] > idx):
                    answer -= 1
                    break
                else:
                    stack.append(idx)
            else:
                stack.append(-1)
    return answer