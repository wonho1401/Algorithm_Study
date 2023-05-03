def solution(storey):
    answer = 0
    s_storey = str(storey)
    length = len(s_storey)
    
    i = 0
    while i != length:
        length = len(s_storey)
        if length == 1:
            if storey > 5:
                answer = 11 - storey
                storey = 0
                break
            else:
                answer = storey
                storey = 0
                break
        if int(s_storey[length - i - 1]) == 0:
            i += 1
            continue
        elif int(s_storey[length - i - 1]) > 5:
            answer += 10 - int(s_storey[length - i - 1])
            storey += 10**(i) * (10 - int(s_storey[length - i - 1]))
        elif int(s_storey[length - i - 1]) < 5:
            answer += int(s_storey[length - i - 1])
            storey -= 10**(i) * int(s_storey[length - i - 1])
        else:
            if int(s_storey[length - i - 2]) >= 5:
                answer += 10 -int(s_storey[length - i - 1])
                storey += 10**(i) *(10 - int(s_storey[length - i - 1]))
            else:
                answer += int(s_storey[length - i - 1])
                storey -= 10**(i) * int(s_storey[length - i - 1])
        i += 1
        s_storey = str(storey)
    if storey != 0:
        answer += 1
    return answer