import math
def solution(r1, r2):
    cnt1, cnt2 = 0, 0
    flag1 = 0
    for i in range(-r2, r2+1):
        cnt2+= 2* int(math.sqrt(r2**2 - i**2))
    cnt2 += (r2)*2 + 1
    
    for i in range(-r1, r1+1):
        cnt1+= 2* int(math.sqrt(r1**2 - i**2))
    cnt1 += (r1)*2 + 1
    
    for i in range(-r1+1, r1):
        if math.sqrt(r1**2 - i**2).is_integer():
            flag1+= 2
    flag1 -= 2
    return cnt2 - cnt1 + 4 + flag1