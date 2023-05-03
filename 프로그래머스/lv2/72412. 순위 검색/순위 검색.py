from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []
    info_dict = {}
    
    for i in range(len(info)):
        _info = info[i].split()
        ikey = _info[:-1]
        ivalue = _info[-1]
        for j in range(5):
            for c in combinations(ikey, j):
                tmp = "".join(c)
                if tmp in info_dict:
                    info_dict[tmp].append(int(ivalue))
                else:
                    info_dict[tmp] = [int(ivalue)]
    for k in info_dict:
        info_dict[k].sort()
    
    for q in query:
        _query = q.split(' ')
        qkey = _query[:-1]
        qvalue = _query[-1]
        
        while 'and' in qkey:
            qkey.remove("and")
        while '-' in qkey:
            qkey.remove('-')
        qkey = "".join(qkey)
        
        if qkey in info_dict:
            scores = info_dict[qkey]
            
            if scores:
                e = bisect_left(scores, int(qvalue))
                answer.append(len(scores) - e)
        else:
            answer.append(0)
    return answer