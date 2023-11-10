def solution(a, b):
    answer = b
    # 1/31, 2/29, 3/31, 4/30, 5/31, 6/30, 7/31, 8/31, 9/30, 10/31, 11/30, 12/31
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    for i in range(a-1):
        answer += days[i]
    return day[answer%7]