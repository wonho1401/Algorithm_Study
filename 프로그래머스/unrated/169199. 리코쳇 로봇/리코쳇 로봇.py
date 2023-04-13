from collections import deque

def in_range(x,y, board):
    return 0<=x< len(board) and 0<=y< len(board[0])

def solution(board):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'R':
                start = [i,j]
            if board[i][j] == 'G':
                end = [i,j]
    visited = []
    q = deque()
    q.append([start[0], start[1], 0])
    
    while q:
        x, y, res = q.popleft()
        print(res)
        if [x, y] in visited:
            continue
        if [x,y] == end:
            return res
        visited.append([x, y])
        for d in range(4):
            nx, ny = x, y
            while True:
                next_x, next_y = nx + dx[d], ny + dy[d]
                if in_range(next_x, next_y, board) and board[next_x][next_y] != 'D':
                    nx, ny = next_x, next_y
                    continue
                q.append([nx, ny, res+1])
                break
    return -1