import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while True:
        if len(scoville) == 1 and scoville[0] < K:
            return -1

        if scoville[0] >= K:
            break
        else:
            min1, min2 = heapq.heappop(scoville), heapq.heappop(scoville)
            scoville.append(min1 + (min2 * 2))
            answer += 1

    return answer

# import heapq

# def solution(scoville, K):
#     answer = 0
#     heapq.heapify(scoville)

#     while scoville[0] < K and len(scoville) > 1:
#         heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
#         answer += 1

#         if len(scoville) == 1 and scoville[0] < K:
#             answer = -1

#     return answer