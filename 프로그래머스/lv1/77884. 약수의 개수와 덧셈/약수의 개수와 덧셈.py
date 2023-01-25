import math
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        cnt = 0
        for j in range(1, int(math.sqrt(i))+1):
            if j**2 == i:
                cnt += 1
            elif i % j == 0:
                cnt += 2
        if cnt % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer