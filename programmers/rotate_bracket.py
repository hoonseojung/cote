def solution(s):
    answer = 0
    for i in range(0, len(s)):
        temp = s[i:] + s[0:i]
        for _ in range(len(s)):
            temp = temp.replace("[]", "")
            temp = temp.replace("{}", "")
            temp = temp.replace("()", "")
            if temp == "":
                answer += 1
                break
    return answer

# def is_valid(s):
#     stack = []
#     for ch in s:
#         if not stack:
#             stack.append(ch)
#         elif stack[-1] == '(':
#             if ch==')': stack.pop()
#             else: stack.append(ch)
#         elif stack[-1] == '{':
#             if ch=='}': stack.pop()
#             else: stack.append(ch)
#         elif stack[-1] == '[':
#             if ch==']': stack.pop()
#             else: stack.append(ch)

#     return False if stack else True

# def solution(s):
#     answer = 0
#     for i in range(len(s)):
#         answer += is_valid(s[i:]+s[:i])
#     return answer