from itertools import permutations

def solution(user_id, banned_id):
    userlist = permutations(user_id, len(banned_id))
    result = []
    for users in userlist:
        flag = True
        for i in range(len(users)):
            user = list(users[i])
            cmp = list(banned_id[i])
            if len(user) == len(cmp):
                for j in range(len(user)):
                    if user[j] != cmp[j] and cmp[j] != '*':
                        flag = False
                        break
            else:
                flag = False
            if not flag:
                break
        if flag:
            if set(users) not in result:
                result.append(set(users))
    return len(result)