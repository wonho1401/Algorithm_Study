import math
def solution(number, limit, power):
    answer = 0
    arr = []
    for i in range(1, number+1):
        divisor = 0
        for j in range(1, int(math.sqrt(i))+1):
            if i % j == 0:
                if math.sqrt(i) == float(j):
                    divisor += 1
                else:
                    divisor += 2
        arr.append(divisor)
    for i in arr:
        if i > limit:
            answer += power
        else:
            answer += i
        
    return answer