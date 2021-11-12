from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    moving = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    now_weight = 0

    while len(moving) > 0:
        answer += 1
        now_weight -= moving.popleft()

        if truck_weights:
            if now_weight + truck_weights[0] <= weight:
                now_weight += truck_weights[0]
                moving.append(truck_weights.popleft())
            else:
                moving.append(0)

    return answer

# from collections import deque

# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     moving = deque([0]*bridge_length)
#     truck_weights = deque(truck_weights)

#     while len(moving) > 0:
#         answer += 1
#         moving.popleft()

#         if truck_weights:
#             if sum(moving)+truck_weights[0] <= weight:
#                 moving.append(truck_weights.popleft())
#             else:
#                 moving.append(0)


#     return answer