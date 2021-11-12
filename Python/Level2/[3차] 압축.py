def solution(msg):
    answer = []
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
    now = ''
    start = 0
    end = start

    while end < len(msg):
        now = msg[start:end + 1]
        if now in alphabet:
            end += 1
        else:
            alphabet.append(now)
            answer.append(alphabet.index(now[:-1]) + 1)
            start = end

    last_word = msg[start:end]
    alphabet.append(last_word)
    answer.append(alphabet.index(last_word) + 1)

    return answer