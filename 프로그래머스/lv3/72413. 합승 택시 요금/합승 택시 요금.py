# n = 노드 수, s = 시작 지점, a= A집 노드, b= B집 노드, fares= 노드 노드 간선
import heapq

INF = int(1e9)

def dijkstra(graph, start):
    distance = [INF]*(len(graph))
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return distance

def solution(n, s, a, b, fares):
    graph= [[] for _ in range(n+1)]
    answer = INF
    for i in range(len(fares)):
        graph[fares[i][0]].append((fares[i][1], fares[i][2]))
        graph[fares[i][1]].append((fares[i][0], fares[i][2]))
    for k in range(1, n + 1):
        dist_k = dijkstra(graph,k)
        answer = min(answer, dist_k[s] + dist_k[a] + dist_k[b])
    return answer