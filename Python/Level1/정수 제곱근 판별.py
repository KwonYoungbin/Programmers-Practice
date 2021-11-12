import math

def solution(n):
    num = math.ceil(n**(1/2))
    return (num+1)**2 if num**2 == n else -1