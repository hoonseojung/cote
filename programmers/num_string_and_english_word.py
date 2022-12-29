def solution(s):
    eng = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    i = 0
    for alphabet in eng:
        s = s.replace(alphabet, str(i))
        i+=1
    return(int(s))