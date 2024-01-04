from collections import deque

def nth_in_range(x, y, n):
    return 0 <= x < n and 0 <= y < n

def solution(n):
    answer = []
    arr = list()
    dx, dy = [1, 0, -1], [0, 1, -1]
    dir, cnt = 0, 1
#   리스트 초기화
    for i in range(n):
        tmp = list()
        for j in range(i+1):
            tmp.append(0)
        arr.append(tmp)
    q = deque()
    x, y = 0, 0
    q.append([x,y])
    arr[x][y] = cnt
    cnt += 1
#   while문 돌기, 종료 조건: cnt == n*(n+1)//2
    while cnt != (n*(n+1) // 2) + 1:
        x, y = q.popleft()
        while True:
            nx, ny = x + dx[dir % 3], y + dy[dir % 3]
#           리스트 범위 체크
            if nth_in_range(nx, ny, n):
#               리스트 방문 체크
                if arr[nx][ny] == 0:
                    q.append([nx, ny])
                    arr[nx][ny] = cnt
                    cnt += 1
                    break
                else:
                    dir += 1
            else:
                dir += 1
    for i in range(n):
        answer += arr[i]
    return answer