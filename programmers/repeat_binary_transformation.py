def solution(s):
    answer = []
    count = 0
    zeros = 0
    while s != "1":
        temp = ''
        for num in s:
            if num == "0":
                zeros += 1
            else:
                temp += num
        s = format(len(temp), 'b')
        count += 1
    answer = [count, zeros]
    return answer