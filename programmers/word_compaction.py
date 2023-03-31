def solution(s):
    if len(s) > 1:
        l = [a for a in range(1, len(s))]
        test = []
        answer = []
        for k in l:
            result = [s[i:i+k] for i in range(0, len(s), k)]
            count = 1
            for j in range(len(result)-1):
                if result[j] == result[j + 1]:
                    count+=1
                    if j == len(result)-2:
                        if count != 1:
                            t = str(count)+result[j]
                            test.append(t)
                else:
                    if count != 1:
                        t = str(count)+result[j]
                        test.append(t)
                        count = 1
                    elif count == 1:
                        test.append(result[j])
                    if j == len(result)-2:
                        test.append(result[j+1])
            tet = ''.join(test)
            answer.append(tet)
            test = []
        return len(min(answer, key=len))
    else:
        return(len(s))
