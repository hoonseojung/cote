tc = int(input())
for test_case in range(1, tc+1):
    num_plate, change_count = input().split()
    change_count = int(change_count)
    n = len(num_plate)
    now = set([num_plate])
    nxt = set()
    for _ in range(change_count):
        while now: # now가 빌 때까지
            s = now.pop() # 리스트(문자열)를 pop
            s = list(s)
            for i in range(n):
                for j in range(i+1, n): # 가능한 모든 경우 확인
                    s[i], s[j] = s[j], s[i]
                    nxt.add(''.join(s)) # 순서를 바꾼 숫자판을 nxt에 추가(set이기에 중복은 알아서 제거)
                    s[i], s[j] = s[j], s[i] # 원상 복구
        now, nxt = nxt, now # 비어있는 now와 이번 회차에서 가능했던 모든 경우의 수의 문자열을 담은 nxt를 교환

    print('#{} {}'.format(test_case, max(map(int, now))))