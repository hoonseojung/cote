def solution(sizes):
    answer = 0
    width, height = [], []
    for size in sizes:
        if size[0] >= size[1]:
            width.append(size[0])
            height.append(size[1])
        else:
            width.append(size[1])
            height.append(size[0])
            
    answer = max(width) * max(height)
    return answer

# -------------------------------------

def solution(sizes):
    answer = 0
    width, height = 0, 0
    for size in sizes:
        if size[0] >= size[1]:
            width = max(width, size[0])
            height = max(height, size[1])
        else:
            width = max(width, size[1])
            height = max(height, size[0])
            
    answer = width * height
    return answer