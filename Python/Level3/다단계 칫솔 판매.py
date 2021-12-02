def solution(enroll, referral, seller, amount):
    answer = []
    dic = {}

    for i in range(len(enroll)):
        dic[enroll[i]] = [[0, referral[i]]]

    for s, a in zip(seller, amount):
        q = [s]
        total = a * 100
        while q:
            now = q.pop()
            ten_per = total // 10
            mine = total - ten_per
            dic[now][0][0] += mine
            if ten_per == 0:
                break

            if dic[now][0][1] != '-':
                q.append(dic[now][0][1])
                total = ten_per

    for key in dic.keys():
        answer.append(dic[key][0][0])
    return answer