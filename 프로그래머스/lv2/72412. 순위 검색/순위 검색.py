from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    answer = []
    dic = defaultdict(list)


    for i in info:
        i = i.split()
        for lang in (i[0], '-'):
            for skill in (i[1], '-'):
                for career in (i[2], '-'):
                    for food in (i[3], '-'):
                        dic[lang + skill + career + food].append(int(i[4]))
    for k in dic:
        dic[k].sort()

    for q in query:
        q = q.split()
        tmp = (q[0]+q[2]+q[4]+q[6])
        if tmp in dic:
            idx = bisect_left(dic[tmp], int(q[7]))
            answer.append(len(dic[tmp]) - idx)
        else:
            answer.append(0)

    return answer