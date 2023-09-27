from collections import Counter
def solution(topping):
    answer = 0
    a = Counter()
    b = Counter(topping)
    for i in range(len(topping)):
        if topping[i] in a:
            a[topping[i]] += 1
        else:
            a[topping[i]] = 1
        b[topping[i]] -= 1
        if b[topping[i]] == 0:
            b.pop(topping[i])
        if len(a) == len(b):
            answer += 1
    return answer