from collections import Counter

def solution(id_list, report, k):
    answer = []
    to = []
    check = []
    dic = {}
    report = list(set(report))
    for i in range(len(report)):
        to.append(report[i].split()[1])
    cnter = Counter(to)
    for i in cnter:
        if cnter[i] >= k:
            check.append(i)
    for i in range(len(report)):
        if report[i].split()[1] in check:
            if report[i].split()[0] in dic:
                dic[report[i].split()[0]] += 1
            else:
                dic[report[i].split()[0]] = 1
    for id in id_list:
        if id in dic:
            answer.append(dic[id])
        else:
            answer.append(0)
    return answer