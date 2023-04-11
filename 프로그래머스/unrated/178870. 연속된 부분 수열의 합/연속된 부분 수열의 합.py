def solution(sequence, k):
    answer = []
    n = len(sequence)
    _k, end = 0, 0
    
    for i in range(len(sequence)):
        while _k < k and end < n:
            _k += sequence[end]
            end += 1
        if _k == k:
            answer.append([i,end-1,end-1-i])
        _k -= sequence[i]
    
    answer = sorted(answer, key= lambda x: x[2])
    return answer[0][:2]