def solution(players, callings):
    dic = {player : i for i, player in enumerate(players)}
    for calling in callings:
        tmp = dic[calling]
        dic[calling] -= 1
        dic[players[tmp - 1]] += 1
        players[tmp], players[tmp-1] = players[tmp-1], players[tmp]
    return players