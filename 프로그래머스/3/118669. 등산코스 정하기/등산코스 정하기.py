import heapq

INF = int(1e9)

def solution(n, paths, gates, summits):
    arr = []
    graph = [[] for _ in range(n+1)]
    for i in range(len(paths)):
        graph[paths[i][0]].append([paths[i][1], paths[i][2]])
        graph[paths[i][1]].append([paths[i][0], paths[i][2]])
    
    q = []
    distance = [INF]* len(graph)
    
    isSummit = [False] * len(graph)
    for summit in summits:
        isSummit[summit] = True
        
    for gate in gates:
        distance[gate] = 0
        heapq.heappush(q,[0, gate])
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist or isSummit[now]:
            continue
        for i in graph[now]:
            i[1] = max(distance[now], i[1])
            if distance[i[0]] > i[1]:
                distance[i[0]] = i[1]
                heapq.heappush(q, [i[1],i[0]])
    for summit in summits:
        arr.append([summit, distance[summit]])
    arr = sorted(arr, key = lambda x: (x[1], x[0]))
    
    return arr[0]