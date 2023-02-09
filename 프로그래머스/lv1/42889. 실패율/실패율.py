from collections import Counter
def solution(N, stages):
    answer = []
    len_stages = len(stages)
    c_stages = Counter(stages)
    for i in range(1,N+1):
        if i in c_stages:
            answer.append(c_stages[i]/len_stages)
            len_stages -= c_stages[i]
        else:
            answer.append(0.0)
    temp = [i for i in range(1, N+1)]
    answer = list(zip(answer,temp))
    answer.sort(key = lambda x:-x[0])
    return [answer[i][1] for i in range(len(answer))]