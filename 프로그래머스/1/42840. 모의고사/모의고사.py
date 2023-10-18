def solution(answers):
    answer = []
    giveup = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    cnt = [[0,1],[0,2],[0,3]]
    for i in range(len(giveup)):
        for j in range(len(answers)):
            if answers[j] == giveup[i][j % len(giveup[i])]:
                cnt[i][0] += 1
    cnt = sorted(cnt, key = lambda x: (-x[0], x[1]))
    answer.append(cnt[0][1])
    if cnt[1][0] == cnt[0][0]:
        answer.append(cnt[1][1])
    if cnt[2][0] == cnt[1][0] and cnt[0][0] == cnt[2][0]:
        answer.append(cnt[2][1])
    return answer