from collections import deque
def solution(n, computers):
    answer = 0
    q = deque()
    visited = [False for _ in range(n)]
    
    for i in range(n):
        if visited[i] == True:
            continue
        else:
            q.append(i)
            answer += 1
            while q:
                tmp = q.popleft()
                for j in range(len(computers[tmp])):
                    if visited[j] == False and computers[tmp][j] == 1:
                        q.append(j)
                        visited[j] = True

    return answer