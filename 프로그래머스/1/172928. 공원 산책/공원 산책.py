def in_bound(x, y, park):
    return 0 <= x < len(park) and 0 <= y < len(park[0])


def solution(park, routes):
    start = [-1, -1]
    dir = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                start = [i, j]

    for i in range(len(routes)):
        op = routes[i].split(" ")[0]
        n = int(routes[i].split(" ")[1])
        tx, ty = start
        flag = True
        for _ in range(n):
            nx, ny = tx + dir[op][0], ty + dir[op][1]
            if in_bound(nx, ny, park) and park[nx][ny] != "X":
                flag = True
                tx, ty = nx, ny
            else:
                flag = False
                break
        if flag:
            start = nx, ny
    return start