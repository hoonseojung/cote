def solution(today, terms, privacies):
    answer = []
    today_l = today.split(".") # today
    terms_l = []
    c = 1
    for t in terms:
        terms_l.append(list(t.split())) # terms
    privacy = []
    for p in privacies:
        privacy.append(list(p.split("."))) # 먼저 .을 구분자로 구분
    for p in privacy:
        d, k = p.pop().split() # 날과 약관 종류가 공백으로 구분되어 있음
        p.append(d)
        p.append(k)
        
    for info in privacy:
        check = [] # 가능 기한
        for t in terms_l: # 해당하는 약관의 유효 기간 k에 저장
            if t[0] == info[3]: 
                k = int(t[1])
                break
        # 연 월 일 순서대로 계산     
        tmp_y = int(info[0]) # 연
        tmp_m = int(info[1]) + k # 월
        tmp_d = int(info[2]) - 1 # 일
        if int(info[1]) + k > 12:
            while tmp_m > 12:
                tmp_m -= 12
                tmp_y += 1
        if tmp_d == 0:
            tmp_m -= 1
            tmp_d = 28
            if tmp_m == 0:
                tmp_y -= 1
                tmp_m = 12
        check.append(tmp_y)
        check.append(tmp_m)
        check.append(tmp_d)

        # check(가능 기한)과 today_l(오늘 날짜) 비교 
        if int(check[0]) < int(today_l[0]): # 연도
            answer.append(c)
        elif int(check[0]) == int(today_l[0]) and int(check[1]) < int(today_l[1]): # 월
            answer.append(c)
        elif int(check[0]) == int(today_l[0]) and int(check[1]) == int(today_l[1]) and int(check[2]) < int(today_l[2]): # 일
            answer.append(c)
        c += 1            
    return answer