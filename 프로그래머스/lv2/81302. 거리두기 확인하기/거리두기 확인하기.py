import math

def check(place):
    players = []
    flag = True
    for i in range(5):
        for j in range(5):
            if place[i][j] == "P":
                players.append([i, j])
    if len(players) == 0 or len(players) == 1:
        return flag
    else:
        for i in range(len(players)):
            for j in range(i+1, len(players)):
                flag = True
                dist = abs(players[i][0]-players[j][0]) + abs(players[i][1] - players[j][1])
                if dist > 2:
                    flag = True
                elif dist < 2:
                    flag = False
                    return flag
                # 맨해튼 거리가 2일 때 그 사이에 파티션이 있는 지 체크하기
                else:
                    # x가 같은 경우에는 둘 사이의 y에 벽
                    if players[i][0] == players[j][0]:
                        if place[players[i][0]][(players[i][1] + players[j][1])//2] == "X":
                            flag = True
                        else:
                            flag = False
                            return flag
                     # y가 같은 경우에는 둘 사이의 x에 벽
                    elif players[i][1] == players[j][1]:
                        if place[(players[i][0] + players[j][0])//2][players[i][1]] == "X":
                            flag = True
                        else:
                            flag = False
                            return flag
                    # 대각선이면 그 반대 대각선 둘 다 벽
                    else:
                        if place[players[i][0]][players[j][1]] == "X" and place[players[j][0]][players[i][1]] == "X":
                            flag = True
                        else:
                            flag = False
                            return flag
    return flag 

def solution(places):
    answer = []
    global players
    # 응시자 위치 담기
    for i in range(len(places)):
        if check(places[i]):
            answer.append(1)
        else:
            answer.append(0)
    return answer
