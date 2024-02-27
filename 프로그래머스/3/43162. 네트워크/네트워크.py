from collections import deque
def solution(n, computers):
    answer = 0
    q = deque()
    
    visit = [False for _ in range(n)]
    
    for i in range(n):
        if visit[i] == True:
            continue
        else:
            q.append(i)
            answer += 1
            while q:
                now_i = q.popleft()
                for j in range(len(computers[now_i])):
                    if visit[j] == False and computers[now_i][j] == 1:
                        q.append(j)
                        visit[j] = True

    return answer