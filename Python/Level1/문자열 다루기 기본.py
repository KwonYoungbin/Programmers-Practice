def solution(s):
    return True if s.isdigit() and len(s) in (4,6)  else False