# 양 끝에서 출발해서 min 풍선까지 최소값을 갱신해 가면서 최소값 이하가 나오는 경우의 개수

def solution(a):
    answer = 1
    point = a.index(min(a)) # 배열의 최소값 index

    temp_min = a[0]
    for i in range(1, point+1):
        if a[i] < temp_min:
            answer += 1
            temp_min = a[i]

    temp_min = a[-1]
    for i in range(len(a)-2, point-1, -1):
        if a[i] < temp_min:
            answer += 1
            temp_min = a[i]
    return answer