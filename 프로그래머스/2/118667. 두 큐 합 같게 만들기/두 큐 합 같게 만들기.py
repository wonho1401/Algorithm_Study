from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1, queue2 = deque(queue1), deque(queue2)
    sq1, sq2 = sum(queue1), sum(queue2)
    
    if (sq1 + sq2) % 2 == 1:
        return -1
    if sq1 == sq2:
        return 0
    while True:
        popq, pop_sum = [queue1, sq1] if sq1 > sq2 else [queue2, sq2]
        insertq, insert_sum  = [queue1, sq1] if sq1 < sq2 else [queue2, sq2]
        
        x = popq.popleft()
        pop_sum -= x
        insertq.append(x)
        insert_sum += x
        
        if sq1 > sq2:
            sq1 = pop_sum
            sq2 = insert_sum
        elif sq1 < sq2:
            sq1 = insert_sum
            sq2 = pop_sum
            
        answer += 1
        
        # 종료 조건
        if sq1 == sq2:
            break
        if answer >= 600000:
            answer = -1
            break
        
    return answer
