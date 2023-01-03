def solution(k, score):
    answer = []
    temp = []
    for i in range(len(score)):
        temp.append(score[i])
        temp.sort(reverse=True)
        if(len(temp) > k):
            del temp[k]
        answer.append(temp[-1])
    return answer