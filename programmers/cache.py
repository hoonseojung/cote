from collections import deque, defaultdict

def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0: return (len(cities) * 5)
    cache = deque()
    cache_check = defaultdict(int)
    
    for city in cities:
        city = city.lower()
        if len(cache) >= cacheSize: # 이때부터 cache 꽉 참
            if cache_check[city] > 0: # 캐시되어 있다면
                cache.remove(city)
                cache.append(city)
                answer += 1
            else: # 캐시되지 않았다면
                citi = cache.popleft()
                cache_check[citi] = 0
                
                cache.append(city)
                cache_check[city] = 1
                answer += 5
        else: # size 공간 존재
            if cache_check[city] > 0: # 캐시되어 있다면
                cache.remove(city)
                cache.append(city)
                answer += 1
            else: # 캐시되지 않았다면
                cache.append(city)
                cache_check[city] = 1
                answer += 5
    return answer