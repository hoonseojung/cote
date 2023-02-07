n = int(input())
row = [0] * n
visited = [0] * n 
result = 0

def promising(x): # 유망 여부 판단
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True

def n_queens(x):
    global result
 
    if x == n:
        result += 1
    else:
        # 각 행에 퀸 놓기
        for i in range(n): # i 는 열번호 0부터 N 전까지 옮겨가면서 유망한 곳 찾기
            if visited[i] == 1:
                continue
            row[x] = i
            if promising(x): # 행, 열, 대각선 체크함수 True이면 백트래킹 안하고 계속 진행
                visited[i] = 1
                n_queens(x + 1)
                visited[i] = 0
 
n_queens(0)
print(result)