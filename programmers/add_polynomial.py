def solution(polynomial):
    answer = ''
    poly = polynomial.split()
    x_sum = 0 # 일차항
    c_sum = 0 # 상수항
    for p in poly:
        if p == '+':
            continue
        if 'x' in p: # 미지수 존재
            p = p[:-1] # x 제외 숫자
            if len(p) > 0: # 계수가 존재했다면
                x_sum += int(''.join(p))
            else: # 계수가 없었다면 = 1
                x_sum += 1
        else: # 상수항
            c_sum += int(p)
    
    # if c_sum == 0 and x_sum > 1: 
    #     answer = str(x_sum) + 'x'
    # elif x_sum == 0 and c_sum > 0:
    #     answer = str(c_sum)
    # elif x_sum == 1 and c_sum > 0:
    #     answer = 'x' + ' + ' + str(c_sum)
    # elif x_sum == 1 and c_sum == 0:
    #     answer = 'x'
    # else:
    #     answer = str(x_sum) + 'x' + ' + ' + str(c_sum)
        
    if x_sum == 0:
        answer = str(c_sum)
    else:
        if x_sum == 1:
            x_sum = ''
        if c_sum == 0:
            c_sum = ''
            answer = str(x_sum) + 'x'
        else:
            answer = str(x_sum) + 'x' + ' + ' + str(c_sum)
    return answer