from collections import defaultdict

def solution(gems):
    answer = []
    items = set(gems)
    dic = defaultdict(int)

    left = 0
    right = 0
    min_length = len(gems) + 1

    while right < len(gems):
        dic[gems[right]] += 1
        right += 1

        if len(dic) == len(items):
            while left < right:
                if dic[gems[left]] > 1:
                    dic[gems[left]] -= 1
                    left += 1
                elif right - left < min_length:
                    min_length = right - left
                    answer = [left + 1, right]
                    break
                else:
                    break
    return answer