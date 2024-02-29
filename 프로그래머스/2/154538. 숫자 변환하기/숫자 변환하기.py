from collections import deque

def operate(x, n):
    return [x+n, x*2, x*3]

def solution(x, y, n):
    if x == y:
        return 0
    else:
        q = deque()
        q.append((x, 0))
        
        visited = [False] * (y+1)
        visited[x] = True

        while q:
            now_x, cnt = q.popleft()
            # operate
            next_x_arr = operate(now_x, n)
            for next in next_x_arr:
                if next == y:
                    return cnt + 1
                elif next < y:
                    if not visited[next]:
                        q.append((next, cnt + 1))
                        visited[next] = True
        return -1