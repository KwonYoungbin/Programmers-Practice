def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if completion[i] != participant[i]:
            return participant[i]

    return participant[-1]

# def solution(participant, completion):
#     answer = ''

#     participant.sort()
#     completion.sort()

#     for i in range(len(completion)):
#         if participant[i] != completion[i]:
#             answer = participant[i]
#             return answer

#     return participant[-1]