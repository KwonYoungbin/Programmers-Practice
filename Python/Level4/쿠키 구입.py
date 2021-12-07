def solution(cookie):
    answer = 0
    m = 0
    while m < len(cookie) - 1:
        left = 0
        right = len(cookie) - 1
        left_sum = sum(cookie[left:m + 1])
        right_sum = sum(cookie[m + 1:right + 1])
        while left <= m and right >= m:
            if left_sum == right_sum:
                if right_sum > answer:
                    answer = right_sum
                break
            elif left_sum < right_sum:
                right_sum -= cookie[right]
                right -= 1
            elif left_sum > right_sum:
                left_sum -= cookie[left]
                left += 1
        m += 1

    return answer