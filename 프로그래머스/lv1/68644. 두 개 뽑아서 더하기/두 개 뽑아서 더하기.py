from itertools import combinations
def solution(numbers):
    c = list(combinations(numbers,2))
    sum_c = []
    for i in c:
        sum_c.append(sum(i))
    sum_c=sorted(list(set(sum_c)))
    return sum_c