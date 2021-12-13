from collections import deque

def solution(arr):
    adder = 0
    arr = deque(arr[::-1])
    min_val = 0
    max_val = 0
    prev = 0
    while arr:
        now = arr.popleft()
        if now == "-":
            temp_min = min_val
            temp_max = max_val
            min_val = min(-(adder + temp_max), -adder + temp_min)
            max_val = max(-(adder + temp_min), -prev + (adder - prev) + temp_max)
            adder = 0
        elif now == '+':
            continue
        else:
            adder += int(now)
            prev = int(now)

    return max_val + adder