def solution(babbling):
    answer = 0
    arr = ["aya", "ye", "woo", "ma"]
    for b in babbling:
        if b in arr:
            answer += 1
        else:
            cur = ""
            acc = ""
            last = ""
            for i in range(len(b)):
                cur += b[i]
                if cur in arr:
                    if last == cur:
                        continue
                    else:
                        acc += cur
                        last = cur
                        cur = ""
            if acc == b:
                answer += 1
    return answer