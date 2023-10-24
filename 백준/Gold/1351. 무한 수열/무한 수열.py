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