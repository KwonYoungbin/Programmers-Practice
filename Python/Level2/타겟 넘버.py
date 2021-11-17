answer = 0


def dfs(arr, idx, target, result):
    global answer
    idx += 1

    if idx == len(arr):
        if result == target:
            answer += 1
        return

    dfs(arr, idx, target, result + arr[idx])
    dfs(arr, idx, target, result - arr[idx])


def solution(numbers, target):
    global answer

    dfs(numbers, 0, target, numbers[0])
    dfs(numbers, 0, target, -1 * numbers[0])
    return answer