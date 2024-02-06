from collections import defaultdict

def solution(files):
    answer = []
    filez = defaultdict()
    for idx, file in enumerate(files):
        head = ""
        number = ""
        for i, f in enumerate(file):
            if not f.isdigit(): # 문자인 경우
                if len(number) > 0: 
                    filez[idx][1] = int(number)
                    break
                else: head += f
            else: # 숫자인 경우
                if len(number) == 0:
                    filez[idx] = [head.lower(), ""]
                number += f
                if i == len(file)-1:
                    filez[idx][1] = int(number)
    filez = sorted(filez.items(), key=lambda x: [x[1][0], x[1][1]])
    answer = [files[file[0]] for file in filez]
    return answer