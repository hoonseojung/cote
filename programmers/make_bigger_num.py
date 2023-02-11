# def solution(number, k):
#     answer = ''
#     n = list(number)
#     index = 0 # 초기값
    # for i in range(len(number)-k):
    #     answer += max(n[index:k+i+1])
    #     index += n[index:k+i+1].index(answer[-1]) + 1

#     print(answer)

#     # test case 10번에서 시간초과 남 ㅠㅡㅠ

def solution(number, k):
    answer = []
    for num in number:
        # answer가 존재하고, k가 0보다 크며, answer의 맨 위 값이 현재의 num보다 작으면
        while answer and k > 0 and answer[-1] < num:
            # answer의 맨 위 값을 제거하고 k도 -1 해준다
            answer.pop()
            k -= 1
        # 현재의 num값은 무조건적으로 answer에 넣어준다
        answer.append(num)
    
    # answer는 (len(number) - k)만큼 슬라이싱 -> 슬라이싱은 index 바깥으로 나가도 ok 
    # 일반적으로 k는 0일텐데 ex) k = 3 number = 1000000 이런 경우엔 k는 처음 그대로 유지됨
    # 이럴 때 답은 뒷 숫자를 k개만큼 없애준 1000이므로 (len(number) - k)만큼 슬라이싱
    answer = ''.join(answer[:len(number)-k])
    
    return answer 
