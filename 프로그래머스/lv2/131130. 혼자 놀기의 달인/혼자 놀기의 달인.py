from copy import deepcopy
# 자연수 하나 정해서 그 수보다 작거나 같은 숫자 카드들 준비
# 카드를 상자에 하나씩 넣고 상자를 무작위로 섞어 일렬로 나열
# 나열되면 순서에 따라 1번부터 순차적으로 index 증가하면서 상자에 붙임
# 상자 하나 선택해서 숫자카드 확인 그 번호의 상자 확인 ..-> 열어야하는 상자가 열려있을때까지
# 그렇게 열린게 1번 그룹, 다 열리면 0점
# 안 열린 상자 임의의 상자 하나 골라서 쭉쭊쭊쭊 -> 2번 상자 그룹
# 1번 그룹 개수 * 2번 그룹 개수 -> return 얻을 수 있는 최고 점수 

# 주어지는 cards[i] = i+1번 상자에 담긴 카드에 적힌 숫자

def solution(cards):
    card = [[0,False]for _ in range(len(cards)) ]
    for i in range(len(cards)):
        card[i][0] = cards[i]
    answer = 0    
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