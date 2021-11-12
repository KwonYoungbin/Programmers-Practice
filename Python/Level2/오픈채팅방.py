def solution(record):
    answer = []
    dic = {}

    for i in record:
        com = i.split()
        if len(com) == 3:
            dic[com[1]] = com[2]

    for i in record:
        com = i.split()
        if com[0] == 'Enter':
            answer.append("%s님이 들어왔습니다." % dic[com[1]])
        elif com[0] == 'Leave':
            answer.append("%s님이 나갔습니다." % dic[com[1]])

    return answer