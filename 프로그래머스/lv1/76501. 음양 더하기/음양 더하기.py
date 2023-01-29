def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        if signs[i]:
            signs[i] = 1
        else:
            signs[i] = -1
    for i in range(len(absolutes)):
        absolutes[i] = signs[i]*absolutes[i]
    return sum(absolutes)