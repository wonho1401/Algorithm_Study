import heapq
INF = int(1e9)

def solution(N, road, K):
    answer = 0
    graph = [[] for i in range(N+1)]
    for i in range(len(road)):
        graph[road[i][0]].append((road[i][1], road[i][2]))
        graph[road[i][1]].append((road[i][0], road[i][2]))
    distance = [INF] * (N + 1)
    q = []
    heapq.heappush(q, (0, 1))
    distance[1] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))
    for i in range(N+1):
        if distance[i] <= K:
            answer += 1
    return answer