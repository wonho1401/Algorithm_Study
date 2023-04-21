from collections import Counter

def solution(weights):
    # 2/3, 2/4, 3/4
    answer = 0
    cnter = Counter(weights)
    
    # 본인들끼리
    for x, y in cnter.items():
        if y >= 2:
            answer += y*(y-1) // 2
            
    weights = list(set(weights))
    
    for weight in weights:
        if weight*(2/3) in weights:
            answer += cnter[weight*(2/3)] * cnter[weight]
        if weight*(2/4) in weights:
            answer += cnter[weight*(2/4)] * cnter[weight]
        if weight*(3/4) in weights:
            answer += cnter[weight*(3/4)] * cnter[weight]
    return answer