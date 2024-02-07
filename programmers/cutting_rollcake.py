from collections import defaultdict

def solution(topping):
    answer = 0
    chulsu = defaultdict(int)
    bro = defaultdict(int)
    top_len = len(topping)
    mid = len(set(topping)) // 2
    for i in range(mid): chulsu[topping[i]] += 1
    for i in range(mid, top_len): bro[topping[i]] += 1
    if len(chulsu) == len(bro): answer += 1
    
    for i in range(mid, top_len-mid):
        chulsu[topping[i]] += 1
        if bro[topping[i]] == 1: 
            del bro[topping[i]]
        else: bro[topping[i]] -= 1
        
        if len(chulsu) == len(bro): answer += 1      
    return answer