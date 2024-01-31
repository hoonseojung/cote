from collections import deque

def h_to_m(book):
    t = []
    for b in book:
        h, m = map(int, b.split(':'))
        t.append(h * 60 + m)
    return t

def solution(book_time):
    answer = 0
    room = []
    books = (h_to_m(book) for book in book_time)
    books = deque(sorted(books, key=lambda x: x[0])) # 시작 시간이 빠른 순서로 정렬

    room.append(books.popleft()[1]) # 첫 퇴실 시간
    
    while books:
        book = books.popleft()
        for i in range(len(room)): # 현재 사용 중인 방들 중     
            if book[0] >= (room[i] + 10): # 입실 시간이 기존 방 (퇴실 시간 + 10분) 이상이라면,
                room[i] = book[1] # 그 방에 입실 = 방 퇴실 시간 갱신
                break
        else: # 시간이 맞는 방이 없으면
            room.append(book[1]) # 새로운 방 필요
    
    answer = len(room)
    return answer