from itertools import combinations

def prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    c = list(combinations(nums,3))
    sum_c = []
    for i in c:
        sum_c.append(sum(i))
    for i in sum_c:
        if prime(i):
            answer += 1

    return answer