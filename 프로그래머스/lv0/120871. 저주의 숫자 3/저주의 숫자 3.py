def solution(n):
    answer = 0
    li = []
    cnt = 1
    for i in range(1, 200):
        if i % 3 == 0 or '3' in str(i):
            continue
        else:
            li.append([cnt, i])
        cnt += 1
    return li[n-1][1]