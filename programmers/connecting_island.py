def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2]) # 비용 기준
    link = set([costs[0][0]]) # 시작 연결점을 set 리스트에 추가
# before : [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
# after : [[0,1,1],[1,3,1],[0,2,2],[1,2,5],[2,3,8]] 

    # Kruskal 알고리즘
    while len(link) != n: # 모든 노드가 연결될 때까지
        for v in costs:
            if v[0] in link and v[1] in link:
                continue # 이미 두 섬이 더 낮은 가격으로 연결되었으니 무시
            if v[0] in link or v[1] in link: # 두 섬 중 하나가 연결되어 있지 않을 때 비용 더하기
                link.update([v[0], v[1]]) # 중복 제거
                answer += v[2] # 간선 비용 더하기
                break
                
    return answer
