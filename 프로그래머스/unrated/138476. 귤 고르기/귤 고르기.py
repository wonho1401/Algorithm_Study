from collections import Counter

def solution(k, tangerine):
    answer = 0
    cnter = Counter(tangerine).most_common()
    for i in range(len(cnter)):
        if cnter[i][1] >= k:
            answer += 1
            break
        else:
            k -= cnter[i][1]
            answer += 1
    return answer