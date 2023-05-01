from collections import deque

def in_range(x,y, maps):
    return 0 <= x < len(maps) and 0 <= y < len(maps[0])

def solution(maps):
    answer = []
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    q = deque()
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]

    for i in range(len(maps)):
        for j in range(len(maps[i])):
            tmp = 0
            if visited[i][j] == True:
                continue
            if maps[i][j] == "X":
                visited[i][j] = True
                continue
            else:
                q.append([i, j])
                visited[i][j] = True
                while q:
                    x, y = q.popleft()
                    tmp += int(maps[x][y])
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if in_range(nx,ny, maps):
                            if visited[nx][ny] == False and maps[nx][ny] != "X":
                                q.append([nx, ny])
                                visited[nx][ny] = True    
                answer.append(tmp)
    if len(answer) == 0:
        return [-1]
    else:
        return sorted(answer)