def combinations(n, arr, new_arr= [], c= 0):
  if n == len(new_arr):
    return [new_arr]
  result = []
  for i in range(c, len(arr)):
    for next_comb in combinations(n, arr, new_arr + [arr[i]], i+1):
      result.append(next_comb)
  return result


N, M = map(int, input().split())

arr = list()

for _ in range(N):
  arr.append(list(map(int, input().split())))

chicken_houses = {}

cnt = 0

for i in range(N):
  for j in range(N):
    if arr[i][j] == 2:
      chicken_houses[cnt] = [i, j]
      cnt += 1

c_idx_arr = [i for i in range(cnt)]

combs = combinations(M, c_idx_arr)

result = int(1e9)

for comb in combs:
  _sum = 0
  for i in range(N):
    for j in range(N):
      if arr[i][j] == 1:
        tmp = int(1e9)
        for k in range(M):
          if arr[i][j] == 1:
            tmp = min(tmp, abs(chicken_houses[comb[k]][0]-i) + 
                abs(chicken_houses[comb[k]][1]-j))
        _sum += tmp
  result = min(result,_sum)
print(result)
