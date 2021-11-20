import math
# 원리를 정확히 이해하지 못함...
def solution(w,h):
    return w*h - (w+h-math.gcd(w,h))