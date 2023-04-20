def solution(picks, minerals):
    mg = list()
    answer = 0
    
    for i in range(0, min(sum(picks)*5,len(minerals)), 5):
        mg.append(minerals[i:i+5])
    
    cost = []
    
    for m in mg:
        tmp = [0,0,0]
        for i in m:
            if i == "diamond":
                tmp[0] += 1
                tmp[1] += 5
                tmp[2] += 25
            elif i == "iron":
                tmp[0] += 1
                tmp[1] += 1
                tmp[2] += 5
            elif i == "stone":
                tmp[0] += 1
                tmp[1] += 1
                tmp[2] += 1
        cost.append(tmp)
    cost.sort(key = lambda x:(-x[2], -x[1]))
    
    for i in cost:
        if picks[0] != 0:
            answer += i[0]
            picks[0] -= 1
        elif picks[1] != 0:
            answer += i[1]
            picks[1] -= 1
        elif picks[2] != 0:
            answer += i[2]
            picks[2] -= 1
    
    return answer