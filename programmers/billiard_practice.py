def solution(m, n, startX, startY, balls):
    answer = []
    # 시작점의 선대칭 점 4개(x, y, x=m, y=n)
    sym = ((startX, -startY), (-startX, startY), (m * 2 - startX, startY), (startX, n * 2 - startY))

    for x, y in balls:
        distances = []
        for x_s, y_s in sym:
            sym_to_start = (startX - x_s)**2+(startY - y_s)**2 # 대칭점에서 시작까지 거리
            sym_to_target = (x - x_s)**2+(y - y_s)**2 # 대칭점에서 타겟까지 거리

            if not (startX==x==x_s or startY==y==y_s) or (sym_to_target > sym_to_start): # 공들이 일직선 상에 있을 때 원쿠를 거쳐가는 것은 포함
                distances.append(sym_to_target)
        answer.append(min(distances)) # 대칭점까지 거리중 최솟값
    return answer
