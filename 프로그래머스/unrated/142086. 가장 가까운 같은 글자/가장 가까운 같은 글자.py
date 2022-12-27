def solution(s):
    answer = []
    for i in range(len(s)):
        tmp = -1
        for j in range(0, i):
            if s[i] == s[j]:
                tmp = i-j
        answer.append(tmp)
    return answer