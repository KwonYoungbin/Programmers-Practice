def time_to_minute(time):
    return int(time[:2]) * 60 + int(time[3:])

def minute_to_time(minutes):
    h = str(minutes // 60).rjust(2, '0')
    m = str(minutes % 60).rjust(2, '0')
    return h + ':' + m

def solution(n, t, m, timetable):
    answer = ''
    next_bus = time_to_minute("09:00")
    for i in range(len(timetable)):
        timetable[i] = time_to_minute(timetable[i])
    timetable.sort(reverse=True)

    last = 0
    while n > 0:
        capacity = m
        while timetable[-1] <= next_bus:
            last = timetable.pop()
            capacity -= 1
            if not timetable or capacity == 0:
                break
        if not timetable and capacity != 0:
            break
        else:
            n -= 1
            if n > 0:
                next_bus += t

    if n > 0 or capacity > 0:
        answer = minute_to_time(next_bus)
    else:
        answer = minute_to_time(last - 1)
    return answer