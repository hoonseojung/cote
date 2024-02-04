# from collections import defaultdict

# def solution(record):
#     history = defaultdict()
#     length = 0
#     for idx, r in enumerate(record):
#         if r[0] == 'L': # Leave
#             user_id = r.split()[1]
#             history[user_id][1].append(["L", idx])
#             length += 1
#         else: # Enter, Change
#             r_s = r.split()
#             act, user_id, name = r_s[0], r_s[1], r_s[2]
#             if act == 'Change': # Change
#                 history[user_id][0] = name
#             else: # Enter
#                 length += 1
#                 if user_id in history:
#                     history[user_id][0] = name
#                     history[user_id][1].append(["E", idx])
#                 else:
#                     history[user_id] = [name, [["E", idx]]]
    
#     answer = [""] * length
    
#     for user_id, val in history.items():
#         name, idxs = val[0], val[1]
        
#         for idx in idxs:
#             if idx[0] == "E": # Enter
#                 answer[idx[1]] = name + "님이 들어왔습니다."
#             else: # Leave
#                 answer[idx[1]] = name + "님이 나갔습니다."
    
from collections import defaultdict

def solution(record):
    answer = []
    history = defaultdict()
    
    for r in record:
        r_s = r.split()
        if len(r_s) == 3: # Enter | Change
            history[r_s[1]] = r_s[2]
    
    for r in record:
        r_s = r.split()
        if r_s[0] == "Enter":
            answer.append("%s님이 들어왔습니다." % history[r_s[1]])
        elif r_s[0] == "Leave":
            answer.append("%s님이 나갔습니다." % history[r_s[1]])
            
    return answer