def solution(files):
    answer = []
    for file in files:
        head, number, tail = '', '', ''
        start_idx = 0
        for s in range(len(file)):
            if not head and file[s].isdigit():
                head = file[:s]
                start_idx = s
            if head and len(number) < 5 and file[s].isdigit():
                number += file[s]
            if number and (not file[s].isdigit() or len(number) > 5):
                tail = file[s:]
                break
        answer.append([head, number, tail])

    answer = [''.join(x) for x in sorted(answer, key=lambda x: (x[0].lower(), int(x[1])))]
    return answer