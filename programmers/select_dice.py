from itertools import combinations, product
from collections import Counter

def solution(dice):
    answer = []
    n = len(dice)
    get_n = n // 2
    all_combinations = list(combinations(range(n), get_n)) # 가능한 조합
    max_win = 0 # 최대 승률
    all_combinations = all_combinations[:len(all_combinations)//2] # 가장 많이 진다는 이야기는 반대 조합일 때 가장 많이 이긴다는 말
    for dice_combi in all_combinations:
        A = [dice[i] for i in dice_combi]
        B = [dice[i] for i in range(n) if i not in dice_combi]
        A_p = list(sum(t) for t in list(product(*A))) # 주사위 눈의 합 가능한 조합
        B_p = list(sum(t) for t in list(product(*B)))
        a_c = Counter(A_p)
        b_c = Counter(B_p)
        a_wins = 0
        b_wins = 0
        for a_k, a_v in a_c.items():
            for b_k, b_v in b_c.items():
                if a_k > b_k: # A 조합이 더 크다면
                    a_wins += a_v * b_v
                elif a_k < b_k: # B 조합이 더 크다면
                    b_wins += a_v * b_v
        if a_wins > b_wins: # A 조합의 승이 크고
            if a_wins > max_win: # 현재까지의 승보다 크다면
                max_win = a_wins
                answer = list(dice+1 for dice in dice_combi) # A 조합의 주사위
        elif a_wins < b_wins: # B 조합의 승이 크고
            if b_wins > max_win: # 현재까지의 승보다 크다면
                max_win = b_wins
                answer = list(i+1 for i in range(n) if i not in dice_combi) # B 조합의 주사위
    return answer