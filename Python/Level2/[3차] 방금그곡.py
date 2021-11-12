def change(info):
    rep = ['H', 'I', 'J', 'K', 'L']  # [A#, C#, D#, E#, F#]
    info = info.replace('A#', rep[0])
    info = info.replace('C#', rep[1])
    info = info.replace('D#', rep[2])
    info = info.replace('F#', rep[3])
    info = info.replace('G#', rep[4])
    return info


def solution(m, musicinfos):
    m = change(m)
    dic = {}

    for music in musicinfos:
        start, end, title, info = music.split(',')
        info = change(info)

        start_h, start_m = map(int, start.split(':'))
        end_h, end_m = map(int, end.split(':'))
        playtime = (end_h - start_h) * 60 + (end_m - start_m)
        playinfo = info * (playtime // len(info)) + info[:playtime % len(info)]

        if m in playinfo:
            dic[title] = playtime

    return sorted(dic, key=lambda x: -dic[x])[0] if dic else "(None)"

# import math

# def change(info):
#     rep = ['H','I','J','K','L'] # [A#, C#, D#, E#, F#]
#     info = info.replace('A#',rep[0])
#     info = info.replace('C#',rep[1])
#     info = info.replace('D#',rep[2])
#     info = info.replace('F#',rep[3])
#     info = info.replace('G#',rep[4])
#     return info

# def solution(m, musicinfos):
#     m = change(m)
#     result = ('(None)', None)

#     for music in musicinfos:
#         start, end, title, info = music.split(',')
#         info = change(info)

#         start_h, start_m = map(int,start.split(':'))
#         end_h, end_m = map(int,end.split(':'))
#         playtime = (end_h-start_h)*60 + (end_m-start_m)
#         playinfo = (info*(math.ceil(playtime/len(info))))[:playtime]

#         if m in playinfo and (result[1] == None or result[1] < playtime):
#             result = (title,playtime)

#     return result[0]