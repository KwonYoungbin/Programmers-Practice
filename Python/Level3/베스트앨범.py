def solution(genres, plays):
    answer = []
    dic = {}
    adder = {}

    for i, genre in enumerate(genres):
        if genre in dic:
            dic[genre].append((plays[i], i))
            adder[genre] += plays[i]
        else:
            dic[genre] = [(plays[i], i)]
            adder[genre] = plays[i]

    adder = sorted(adder, key=lambda x: adder[x], reverse=True)

    for key in dic.keys():
        dic[key].sort(key=lambda x: (-x[0], x[1]))

    for genre in adder:
        if len(dic[genre]) == 1:
            answer.append(dic[genre][0][1])
        else:
            answer.append(dic[genre][0][1])
            answer.append(dic[genre][1][1])

    return answer