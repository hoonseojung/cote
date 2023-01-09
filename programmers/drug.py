# '''
# 약 N개
# i번째 약 먹은날 포함하여 D_i 일 후부터 E_i만큼 약효 발현
# 여러 약 투약 -> 약효 누적
# 하루에 최대 하나의 약만 투여 가능, 한번 사용한 약은 다시 투여 X
# 오늘(1일)부터 투약 시작하여 X일에 얻을 수 있는 누적 약효의 최댓값?

# 입력 형식 
# 1. 첫째줄에 약 개수 N, 날짜 X일 입력
# 2. N개의 줄에 약효 발현되는데 소요되는 날짜 D_i일, 약효 E_i일 입력
# '''

# # TC 1, ans : 15
# 3 2
# 1 10
# 1 1
# 2 5

# # TC 2, ans : 155
# 5 3
# 2 100
# 3 5
# 1 50
# 1 1
# 4 100

# # TC 3, ans : 17
# 5 5
# 3 5
# 1 3
# 2 4
# 2 4
# 3 1

n, x = map(int, input().split())

drug_list = [[] * n for _ in range(n)]
dur = 0 # 누적 약효 시간
count = x # 개수 제한

for i in range(n):
    d, e = map(int, input().split())
    drug_list[i] = [d, e]

drug_list = sorted(drug_list, key=lambda x: (-x[0], -x[1])) # 발현 시간이 긴 순서대로, 약효가 긴 순서대로

for i in range(n):
    if count > 0:
        if drug_list[i][0] <= x:
            dur += drug_list[i][1]
            count -= 1

print(dur)