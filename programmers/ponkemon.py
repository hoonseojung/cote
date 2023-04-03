def solution(nums):
    answer = 0
    num = set(nums)
    if len(num) >= len(nums) // 2: # 종류가 매우 다양한 경우
        return len(nums) // 2
    else: # 종류가 별로 없는 경우
        return len(num)