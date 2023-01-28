def solution(lottos, win_nums):
    answer = []
    cnt, zero_cnt = 0, 0
    for lotto in lottos:
        if lotto in win_nums:
            cnt += 1
    zero_cnt = lottos.count(0)
    if cnt == 0 and zero_cnt ==0:
        answer.append(6-(cnt+zero_cnt))
    else:
        answer.append(7-(cnt+zero_cnt))
    if cnt == 0:
        answer.append(6-cnt)
    else:
        answer.append(7-cnt)
    return answer