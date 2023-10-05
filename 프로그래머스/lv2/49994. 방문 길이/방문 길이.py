def solution(dirs):
    route = list()
    start = [0,0]
    route.append(start)
    dir = {"U":[0,1], "R":[1,0], "D":[0, -1], "L":[-1, 0]}
    for d in dirs:
        nx = start[0] + dir[d][0]
        ny = start[1] + dir[d][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            start = [nx, ny]
            if dirs.index(d) == len(dirs):
                route.append([nx,ny])
            if start not in route:
                route.append([nx,ny])
    return len(route)