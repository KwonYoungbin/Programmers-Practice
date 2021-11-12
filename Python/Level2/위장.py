def solution(clothes):
    answer = 1
    dic = {}

    for v, k in clothes:
        if k in dic:
            dic[k].append(v)
        else:
            dic[k] = [v]

    for i in dic.keys():
        answer *= (len(dic[i]) + 1)
    return answer - 1

# def solution(clothes):
#     answer = 1
#     kinds = {}

#     for _hash in clothes:
#         val = _hash[0]
#         key = _hash[1]
#         if key in kinds:
#             kinds[key].append(val)
#         else:
#             kinds[key] = [val]

#     for i in kinds.keys():
#         answer *= (len(kinds[i])+1)

#     answer -= 1
#     return answer