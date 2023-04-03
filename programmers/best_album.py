from collections import defaultdict
def solution(genres, plays):
    answer = []
    album = defaultdict(int)
    for gen in set(genres):
        album[gen] = 0
    for i in range(len(genres)):
        album[genres[i]] += plays[i]
    album = dict(sorted(album.items(), key=lambda x: -x[1]))
    # album = {'pop': 3100, 'classic': 1450}
    for gen in album:
        temp = []
        for i in range(len(genres)):
            if genres[i] == gen:
                temp.append([i, plays[i]])
        temp = sorted(temp, key=lambda x: (-x[1], x[0]))
        answer.append(temp[0][0])
        if len(temp) >= 2:
            answer.append(temp[1][0])
    return answer


#############################################################
# 생각해볼만한 코드
# def solution(genres, plays):
#     answer = []
#     dic = {}
#     album_list = []
#     for i in range(len(genres)):
#         dic[genres[i]] = dic.get(genres[i], 0) + plays[i]
#         album_list.append(album(genres[i], plays[i], i))

#     dic = sorted(dic.items(), key=lambda dic:dic[1], reverse=True)
#     album_list = sorted(album_list, reverse=True)



#     while len(dic) > 0:
#         play_genre = dic.pop(0)
#         print(play_genre)
#         cnt = 0;
#         for ab in album_list:
#             if play_genre[0] == ab.genre:
#                 answer.append(ab.track)
#                 cnt += 1
#             if cnt == 2:
#                 break

#     return answer

# class album:
#     def __init__(self, genre, play, track):
#         self.genre = genre
#         self.play = play
#         self.track = track

#     def __lt__(self, other):
#         return self.play < other.play
#     def __le__(self, other):
#         return self.play <= other.play
#     def __gt__(self, other):
#         return self.play > other.play
#     def __ge__(self, other):
#         return self.play >= other.play
#     def __eq__(self, other):
#         return self.play == other.play
#     def __ne__(self, other):
#         return self.play != other.play