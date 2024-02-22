def h_diff(h1, h2):
    ha, ma = h1.split(":")
    hb, mb = h2.split(":")
    return (int(hb)*60 + int(mb)) - (int(ha)*60 + int(ma))

def down_shop(ss):
    if ss.count("#"):
        ss = ss.split("#")
        for i in range(len(ss)-1):
            s = list(ss[i])
            s[-1] = s[-1].lower()
            ss[i] = ''.join(s)
        return ''.join(ss)
    else: return ss

def solution(m, musicinfos):
    answer = "(None)"
    max_time = 0
    m = down_shop(m)
    for music in musicinfos:
        music = music.split(",")
        play_time = h_diff(music[0], music[1])
        music[3] = down_shop(music[3])
        music_len = len(music[3])
        if play_time > music_len:
            melody = music[3]*(play_time//music_len) + music[3][:play_time%music_len]
        else: melody = music[3][:play_time]
        if (m in melody) and (max_time < play_time): 
            answer = music[2]
            max_time = play_time
    return answer