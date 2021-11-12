def solution(x):
    sum_val = sum([int(a) for a in str(x)])
    return True if x % sum_val == 0 else False