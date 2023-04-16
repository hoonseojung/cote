from collections import Counter
def solution(X, Y):
    answer = ''
    x = Counter(X)
    y = Counter(Y)
	# X :  Counter({'0': 2, '1': 1})
	# Y :  Counter({'2': 1, '3': 1, '4': 1, '5': 1})
    for i in x:
        cnt = 0
        if i in y: # x에 있는 숫자가 y에도 있다면
            cnt = min(x[i], y[i]) # 둘 중 더 적게 나오는 횟수
        for j in range(cnt): # 만큼
            answer += i # 해당 숫자를 answer에 더하기
    
    if answer == '': # 짝꿍이 없다면
        return "-1"
    
    answer = sorted(answer, reverse=True) # 있다면 내림차순으로 정렬
    
    if answer[0] == '0': # 정렬 후에도 첫 index가 0이라면, 0 00 000 .. 중 하나
        return "0"
    
    return ''.join(answer)