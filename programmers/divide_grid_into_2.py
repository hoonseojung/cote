from collections import deque

def solution(n, wires):
    answer = 1000
    wires = [[i-1, j-1] for i, j in wires]
    trees = [[] for _ in range(n)]
    for wire in wires:
        trees[wire[0]].append(wire[1])
        trees[wire[1]].append(wire[0])
    
    def bfs(n1, n2):
        count = 1
        queue = deque([n1])
        visited[n1] = True
        while queue:
            node = queue.popleft()
            for nodes in trees[node]:
                if not visited[nodes] and nodes != n2:
                    count += 1
                    visited[nodes] = True
                    queue.append(nodes)
        return count
    
    for wire in wires:
        visited = [False for _ in range(n)]
        answer = min(answer, abs(n-(bfs(wire[0], wire[1])*2)))
    return answer