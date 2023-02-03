def solution(emergency):
    answer = []
    emer = sorted(emergency, reverse=True)
    for patient in emergency:
        answer.append(emer.index(patient)+1)
    return answer