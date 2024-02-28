def solution(name, yearning, photo):
    answer = []
    dic = {}
    for n, y in zip(name, yearning):
        dic[n] = y

    for piece in photo:
        cnt = 0
        for person in piece:
            if person in name:
                cnt += dic[person]
        answer.append(cnt)
    return answer