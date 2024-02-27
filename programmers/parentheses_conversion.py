# 문자열 w를 두 균형잡힌 괄호 문자열 u, v로 분리하는 함수
def u_v_split(lst):
    left_cnt = 0
    right_cnt = 0
    idx = 0
    for i in range(len(lst)):
        if lst[i] == '(': left_cnt += 1
        elif lst[i] == ')': right_cnt += 1
        if left_cnt == right_cnt:
            idx = i
            break
    u, v = lst[:(idx+1)], lst[(idx+1):]
    return (u, v)

# 올바른 괄호 문자열인지 확인하는 함수
def check_right(u):
    stck = [] # '(' append
    idx = 0
    while idx < len(u):
        cur_idx = u[idx]
        if not stck: stck.append(cur_idx)
        elif (stck[-1] == '(') and (cur_idx == ')'): stck.pop(-1)
        else: stck.append(cur_idx)
        idx += 1
    if stck: return False
    else: return True

# 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행하는 함수. 
def del_convert(string_val):
    string_val.pop(0)
    string_val.pop(-1)
    if not string_val: return []
    else:
        for i in range(len(string_val)):
            if string_val[i] == '(': string_val[i] = ')'
            else: string_val[i] = '('
        return string_val

def step(w):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
    if len(w) == 0: return []
    
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 
    # 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
    u, v = u_v_split(w)
    
    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
    # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
    if check_right(u): return u + step(v)

    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
    else:
        # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
        # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
        # 4-3. ')'를 다시 붙입니다.
        # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
        new_u = del_convert(u)
        # 4-5. 생성된 문자열을 반환합니다.
        return ['('] + step(v) + [')'] + new_u
        
def solution(p):
    p = list(p)
    return (''.join(step(p)))