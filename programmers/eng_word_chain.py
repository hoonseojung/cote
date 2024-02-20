from collections import defaultdict
def solution(n, words):
    answer = [0, 0]
    history = defaultdict(int)
    people = n
    past = words[0]
    for i, word in enumerate(words):
        num = (i // n) + 1
        if history[word] > 0:
            if (i+1)%n: people = (i+1)%n
            answer = [people, num]
            break
        else:
            history[word] = 1
            if i:
                if word[0] != past[-1]:
                    if (i+1)%n: people = (i+1)%n
                    answer = [people, num]
                    break
                past = word
    return answer