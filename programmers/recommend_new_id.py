def solution(new_id):
    special_char = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '=', '+', '[', '{', ']', '}', ':', '?', ',', '<', '>', '/']
    
    new_id = new_id.lower() # 1단계
    
    for s in special_char: # 2단계
        if s in new_id:
            new_id = new_id.replace(s, "")
    
    if '..' in new_id: # 3단계
        while '..' in new_id:
            new_id = new_id.replace('..', '.')
    
    if len(new_id) > 0:  # 4단계
        if new_id[0] == '.':
            new_id = new_id[1:]
    if len(new_id) > 0:
        if new_id[-1] == '.':
            new_id = new_id[:-1]
        
    if new_id == "": # 5단계
        new_id += 'a'
        
    if len(new_id) >= 16: # 6단계
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    
    if len(new_id) <= 2: # 7단계
        while len(new_id) != 3:
            new_id += new_id[-1]
            
    return new_id
# ------------------------------------------
# 정규식
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st