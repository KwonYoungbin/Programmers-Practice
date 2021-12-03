def cal_seconds(time):
    h = int(time[:2]) * 3600
    m = int(time[3:5]) * 60
    s = int(time[6:])
    return h + m + s

def time_to_string(time):
    h = str(time // 3600).rjust(2, '0')
    m = str((time % 3600) // 60).rjust(2, '0')
    s = str((time % 3600) % 60).rjust(2, '0')
    return ':'.join([h, m, s])

def solution(play_time, adv_time, logs):
    if play_time == adv_time:
        return "00:00:00"
    play_time = cal_seconds(play_time)
    adv_time = cal_seconds(adv_time)
    arr = [0 for _ in range(play_time + 1)]

    for log in logs:
        start = cal_seconds(log[:8])
        end = cal_seconds(log[9:])
        arr[start] += 1
        arr[end] -= 1

    for i in range(1, len(arr)):
        arr[i] += arr[i - 1]

    for i in range(1, len(arr)):
        arr[i] += arr[i - 1]

    max_cnt = 0
    largest = arr[adv_time - 1]
    for i in range(adv_time, play_time):
        if largest < arr[i] - arr[i - adv_time]:
            largest = arr[i] - arr[i - adv_time]
            max_cnt = i - adv_time + 1

    return time_to_string(max_cnt)