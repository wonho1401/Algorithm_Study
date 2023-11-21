def compare(s, num, dic):
    if num == 4:
        return
    elif num > 4:
        dic[s[1]] += (num - 4)
    elif num < 4:
        dic[s[0]] += (4 - num)
    return

def solution(survey, choices):
    dic = {'A':0,'N':0,'C':0,'F':0,'M':0,'J':0,'R':0,'T':0}
    arr = [['R','T'],['C','F'],['J','M'],['A','N']]
    answer = ''
    for s, c in zip(survey, choices):
        compare(s, c, dic)
    for a in arr:
        answer += a[1] if dic[a[0]] < dic[a[1]] else a[0]
    return answer