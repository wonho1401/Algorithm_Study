# 주어진 N의 크기가 10^9를 넘어가면 dictionary와 재귀를 사용해 해결하도록 생각해보기

n, p, q = map(int, input().split())

dic = {}
dic[0] = 1


def recursive(num):
    if num in dic:
        return dic[num]
    else:
        dic[num] = recursive(num//p) + recursive(num//q)
        return dic[num]


print(recursive(n))
