import heapq

def solution(n, k, enemy):
    answer = 0
    e = 0
    heap = []
    for i in range(len(enemy)):
        e += enemy[i]
        heapq.heappush(heap, -enemy[i])
        if e> n:
            if k == 0:
                return i
            e += heapq.heappop(heap)
            k -= 1
    return i+1