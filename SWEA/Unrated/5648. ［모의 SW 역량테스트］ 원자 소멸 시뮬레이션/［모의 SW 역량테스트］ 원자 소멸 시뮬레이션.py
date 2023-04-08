T = int(input())

dx = [0, 0, -0.5, 0.5]
dy = [0.5, -0.5, 0, 0]

for t in range(T):
    N = int(input())
    ans = 0
    atoms = [list(map(int, input().split())) for _ in range(N)]
    # [0] = x좌표  [1] = y좌표 [2]= 이동 방향 [3] = 보유 에너지
    while len(atoms) >= 2:
        for i in range(len(atoms)):
            atoms[i][0] += dx[atoms[i][2]]
            atoms[i][1] += dy[atoms[i][2]]
        dic = {}
        for atom in atoms:
            try:
                dic[(atom[0], atom[1])].append(atom)
            except:
                dic[(atom[0], atom[1])] = [atom]

        atoms = []

        for d in dic:
            if len(dic[d]) >= 2:
                for atom in dic[d]:
                    ans += atom[3]
            else:
                if -1000 <= dic[d][0][0] <= 1000 and -1000 <= dic[d][0][1] <= 1000:
                    atoms.append(dic[d][0])
    print(f'#{t+1}', ans)