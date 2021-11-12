def solution(brown, yellow):
    answer = [3,3]
    for y in range(1, int(yellow//2)+1):
        if yellow % y == 0:
            x = yellow//y
            if 2*(x+y+2) == brown:
                answer = [x+2,y+2]
                break
    return answer