N, M = map(int, input().split())
N_list = list(map(int, input().split()))

res = 0
left = 0
right = max(N_list)

while left <= right:
    cnt = 0
    mid = (left + right) // 2

    for x in N_list:
        if mid < x:
            cnt += (x - mid)

    if cnt >= M:
        res = mid
        left = mid + 1
    else:
        right = mid - 1

print(res)