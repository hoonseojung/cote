n = int(input())
weights = sorted(list(map(int, input().split())))
answer = 1

for i in range(n):
    if answer < weights[i]: # 추가 무게보다 더 무겁다면
        break 
    answer += weights[i] # 추가 무게 이하라면 무게에 더하기
print(answer)
