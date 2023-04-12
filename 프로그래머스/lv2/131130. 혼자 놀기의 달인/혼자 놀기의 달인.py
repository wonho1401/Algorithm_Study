from copy import deepcopy

def solution(cards):
    card = [[0,False]for _ in range(len(cards)) ]
    for i in range(len(cards)):
        card[i][0] = cards[i]
    fb = []
    cnt = []
    for i in range(len(cards)):
        fb = []
        tmp = deepcopy(card)
        fb.append(cards[i])
        x = cards[i]
        while True:
            if tmp[cards[x - 1] - 1][1] == True:
                break
            tmp[cards[x - 1] - 1][1] = True
            x = cards[x - 1]
            fb.append(x)
        fb = list(set(fb))
        cnt.append(len(fb))
    cnt = sorted(list(set(cnt)), reverse= True)
    if cnt[0] == len(cards) or 0:
        return 0
    elif len(cnt) == 1:
        return cnt[0]*cnt[0]
    else:
        return cnt[0]*cnt[1]
