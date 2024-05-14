from collections import deque

def in_range(x, y, maps):
    return 0 <= x < len(maps) and 0 <= y < len(maps[0])

def solution(maps):
    answer = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    q = deque()
    start = [0, 0]
    q.append(start)
    visited[start[0]][start[1]] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if in_range(nx, ny, maps) and not visited[nx][ny] and maps[nx][ny] == 1:
                visited[nx][ny] = True
                maps[nx][ny] = maps[x][y] + 1
                q.append([nx, ny])
    return maps[-1][-1] if maps[-1][-1] > 1 else -1