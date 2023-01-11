from collections import Counter

def solution(X, Y):
    answer = '-1'
    sx, sy = set(list(X)), set(list(Y))
    cx, cy = Counter(list(X)), Counter(list(Y))
    
    intersection = sx & sy
    if intersection:
        answer =''
        sortNum = sorted(intersection, reverse=True)
        for num in sortNum:
            answer += num * min(cx[num], cy[num])
        if len(answer) == answer.count('0'):
            answer = '0'
        elif len(answer) == 0:
            answer = '-1'
    return answer