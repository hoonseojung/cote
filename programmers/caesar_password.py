def solution(s, n):
    answer = ""
    for i in s:
        if i == ' ':
            answer += i
            continue
        else:            
            c = chr(ord(i) + n) if (65 <= (ord(i) + n) <= 90) or ((97 <= ord(i)) and (97 <= (ord(i) + n) <= 122)) else chr(ord(i) + n - 26)
        answer += c
    return answer