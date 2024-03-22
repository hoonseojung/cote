def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    
    set1 = list()
    set2 = list()
    
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            set1.append(str1[i]+str1[i+1])
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            set2.append(str2[i]+str2[i+1])
    if len(set1) == 0 and len(set2) == 0: answer = 1
    else:
        # intersection
        intersect = list()
        temp = set2.copy()
        for s in set1:
            if s in temp:
                intersect.append(s)
                temp.remove(s)

        # union
        union = len(set1) + len(set2) - len(intersect)

        answer = len(intersect)/union
    answer = int(65536 * answer)
    return answer