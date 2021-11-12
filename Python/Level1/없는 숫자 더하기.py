def solution(numbers):
    num_arr = [0,1,2,3,4,5,6,7,8,9]
    return sum(num_arr) - sum(numbers)

# def solution(numbers):
#     answer = 0
#     for i in range(10):
#         if i not in numbers:
#             answer += i
#     return answer