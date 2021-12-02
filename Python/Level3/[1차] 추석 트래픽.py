def cal_endtime(time):
    h = int(time[:2]) * 3600
    m = int(time[3:5]) * 60
    s = int(time[6:8])
    ms = int(time[9:])
    return (h + m + s) * 1000 + ms

def cal_starttime(time, job):
    job = int(float(job) * 1000)
    return cal_endtime(time) - job + 1

def solution(lines):
    answer = 0
    if len(lines) == 1:
        return 1

    starttime = []
    endtime = []

    for line in lines:
        day, time, job = line.split()
        endtime.append(cal_endtime(time))
        starttime.append(cal_starttime(time, job[:-1]))

    for i in range(len(lines) - 1):
        cnt = 1
        for j in range(i + 1, len(lines)):
            if endtime[i] > starttime[j] - 1000:
                cnt += 1
        answer = max(answer, cnt)

    return answer