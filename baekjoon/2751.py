import sys
n = int(sys.stdin.readline())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline()))
nums.sort()
for num in nums:
    print(num)

# input() 이 sys.stdin.readline() 보다 느린 이유 :
# input() 내장 함수는 sys.stdin.readline()과 비교해서 prompt message를 출력하고,
# 개행 문자를 삭제한 값을 리턴하기 때문에 느리다.

# input() 과 sys.stdin.readline() 의 차이점 :
# 일단 sys.stdin.readline()과 input()은 같은 역할을 하지 않는다.
# input() 내장 함수는 parameter로 prompt message를 받을 수 있다
# 따라서 입력받기 전 prompt message를 출력해야 한다
# 물론 prompt message가 없는 경우도 있지만, 이 경우도 약간의 부하로 작용할 수 있다
# 하지만, sys.stdin.readline()은 prompt message를 인수로 받지 않는다.
# 또한, input() 내장 함수는 입력받은 값의 개행 문자를 삭제시켜서 리턴한다
# 즉 입력받은 문자열에 rstrip() 함수를 적용시켜서 리턴한다
# 반면에 sys.stdin.readline()은 개행 문자를 포함한 값을 리턴한다. 이 때문에 조금 귀찮은 점이 있기도 하다.

# 정렬 직접 구현
n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])
    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]: # 두개의 배열에서 순서대로 원소 비교
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr

nums = merge_sort(nums)

for num in nums:
    print(num)