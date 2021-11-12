def solution(s):
    num_s = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(num_s)):
        s = s.replace(num_s[i], str(i))

    return int(s)