def solution(wallpaper):
    answer = []
    x = []
    y = []
    # lux 최소, rdy 최대
    for i in range(len(wallpaper)):
        if "#" in wallpaper[i]:
            x.append(i)
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if "#" in wallpaper[i][j]:
                y.append(j)
    answer = [min(x),min(y), max(x)+1, max(y)+1]
    return answer