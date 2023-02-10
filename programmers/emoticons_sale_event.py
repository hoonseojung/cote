from itertools import combinations_with_replacement
def solution(users, emoticons):
    answer = []
    sales = [10, 20, 30, 40] * (len(emoticons))
    sale_cb = list(set(combinations_with_replacement(sales, len(emoticons)))) # 가능한 모든 조합
    price = 0 # 가격
    plus = 0 # 서비스 가입 수
    total = 0 # 최종 판매액

    for sale in sale_cb: # 할인율 한 개의 조합에 대해
        for user in users: # 유저 1명 별
            for i in range(len(emoticons)): # 구매 가능 여부 확인
                if user[0] <= sale[i]: # 해당 상품의 할인율이 기준치 이상이라면
                    price += emoticons[i] * ((100 - sale[i]) / 100) # 가격 구하기
            if price >= user[1]: # 구한 가격이 기준치 이상이라면
                plus += 1 # 이모티콘 플러스 서비스 가입
            else: # 기준치 미만이라면 이모티콘 구매
                total += price # 판매액 갱신
            price = 0 # 가격 초기화
        answer.append([plus, total])
        plus, total = 0, 0 # 초기화

    answer = sorted(answer, key = lambda x: (-x[0], -x[1])) # 서비스 가입자 수가 많은 순서대로, 가입자 수가 같다면 판매액이 큰 순서대로 정렬
    return answer[0]