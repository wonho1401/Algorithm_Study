def solution(sizes):
    for size in sizes:
        if size[0] < size[1]:
            size[0], size[1] = size[1], size[0]
    maxX, maxY = 0, 0
    for i in range(len(sizes)):
        if maxX < sizes[i][0]:
            maxX = sizes[i][0]
        if maxY < sizes[i][1]:
            maxY = sizes[i][1]
    return maxX*maxY