from collections import Counter

def solution(participant, completion):
    answer = ''
    p = Counter(participant)
    c = Counter(completion)
    return "".join(p-c)