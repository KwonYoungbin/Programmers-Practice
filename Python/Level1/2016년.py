def solution(a, b):
    answer = ''
    days_of_months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    weeks = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']

    if a == 1:
        return weeks[(b - 1) % 7]
    else:
        return weeks[(b + sum(days_of_months[:a - 1]) - 1) % 7]
    return answer