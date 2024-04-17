N = int(input())
U = set()

for _ in range(N):
  U.add(int(input()))

S = set()
for i in U:
  for j in U:
    S.add(i + j)

arr = list()

for i in U:
  for j in U:
    if (i-j) in S:
      arr.append(i)
arr.sort(reverse=True)
print(arr[0])