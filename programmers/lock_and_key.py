import copy

def solution(key, lock):
    answer = False
    M = len(key)
    N = len(lock)
    keys = []
    locks = []
    
    for i in range(M):
        for j in range(M):
            if key[i][j] == 1: keys.append([i, j]) # key는 (0, 0)부터 시작
    keys_len = len(keys)

    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0: 
                locks.append([i+M-1, j+M-1]) # lock은 (M-1, M-1)부터 시작
    
    def rotate_90(keys): # 시계 방향으로 90도 회전
        key_90 = []
        for k in keys:
            key_90.append([k[1], M-k[0]-1])
        return key_90
    
    def rotate_180(keys): # 180도
        key_180 = []
        for k in keys:
            key_180.append([M-k[0]-1, M-k[1]-1])
        return key_180
    
    def rotate_270(keys): # 270도 = -90도
        key_270 = []
        for k in keys:
            key_270.append([M-k[1]-1, k[0]])
        return key_270
    
    def check_key(moved_key): # 이동된 키가 홈과 맞는지 확인하는 함수
        if len(moved_key) < len(locks): return False # 애초에 홈을 전부 채우지 못 한다면 False
        checking = 0
        for k in moved_key: # 이동된 키가
            if k in locks: checking += 1 # 홈을 채운다면 +1
            elif ((M-1) <= k[0] <= (N+M-2)) and ((M-1) <= k[1] <= (N+M-2)): return False # 홈을 채우지 못 하면서 자물쇠의 돌기와 만난다면 False
        if checking == len(locks): return True # 돌기를 만나지 않으면서 홈을 다 채울 수 있다면 True
        return False
       
    def move_key(rotated_keys): # 회전된 키를 차례대로 이동시키며 확인하는 함수
        for i in range(N+M-1): # 이동 자체를 N+M-1번 움직임
            moved_key = copy.deepcopy(rotated_keys) # 2차원 배열로 deepcopy
            for k in range(keys_len):
                moved_key[k][0] = rotated_keys[k][0] + i # 우로
            for j in range(N+M-1):
                for k in range(keys_len):
                    moved_key[k][1] = rotated_keys[k][1] + j # 좌에서
                if check_key(moved_key): return True
        return False

    if move_key(keys): return True # 0도 회전한 키
    
    key_90 = rotate_90(keys) 
    if move_key(key_90): return True
    
    key_180 = rotate_180(keys)
    if move_key(key_180): return True

    key_270 = rotate_270(keys)
    if move_key(key_270): return True

    return answer
