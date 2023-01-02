def solution(s):
    answer, i = 0, 0
    tmp1, tmp2 = 1, 0
    while(len(s) > 0):
        if len(s) == i+1:
            answer += 1
            break
        if s[0] != s[i+1]:
            tmp2 +=1
        elif s[0] == s[i+1]:
            tmp1 += 1
        if(tmp1 == tmp2):
                answer += 1
                s = s[i+2:]
                tmp1 , tmp2, i = 1, 0, 0
        else:
             i += 1   
    return answer