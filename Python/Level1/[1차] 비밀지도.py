def solution(n, arr1, arr2):
    answer = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        arr1_now = format(arr1[i], 'b')
        arr2_now = format(arr2[i], 'b')
        s = str(int(arr1_now) + int(arr2_now)).rjust(n, '0')

        answer[i] = s.replace('0', ' ').replace('1', '#').replace('2', '#')

    return answer