def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(len(score)):
        if i % m == m-1:
            answer += score[i]*m
    return answer