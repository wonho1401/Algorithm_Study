def solution(keymap, targets):
    answer = []
    dic = {}
#   keymap에서 각 알파벳이 존재하는 최소 index dictionary 생성
    for key in keymap:
        for i in range(len(key)):
            if key[i] in dic:
                if dic[key[i]] > i+1:
                    dic[key[i]] = i+1
                else:
                    continue
            else:
                dic[key[i]] = i+1
#   targets 값 찾기
    for target in targets:
        tmp = 0
        for i in range(len(target)):
            if target[i] not in dic:
                tmp = -1
                break
            else:
                tmp += dic[target[i]]
        answer.append(tmp)
    return answer