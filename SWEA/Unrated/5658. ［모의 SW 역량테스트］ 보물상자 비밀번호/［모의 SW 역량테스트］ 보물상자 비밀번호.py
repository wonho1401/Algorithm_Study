T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    numbers = list(input())
    tmp_set = set()
    for _ in range(N//4):
        tmp = numbers.pop()
        numbers.insert(0, tmp)
        for i in range(0, len(numbers), N//4):
            tmp_str = ''
            tmp_str += ''.join(numbers[i:i+N//4])
            tmp_set.add(tmp_str)
    tmp_list = sorted(tmp_set, reverse=True)
    print('#%d %d'%(t,int(tmp_list[K-1], 16)))