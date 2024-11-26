from collections import deque

def solution(elements):

    queue1 = deque(elements)
    queue2 = deque(elements)
    sumq = 0
    answer = 0
    result = set(elements)
    lene = len(elements)
    
    for i in range(lene):
        answer = queue1.popleft()
        for j in range(i+1, i+lene):
            answer += elements[j%lene]
            result.add(answer)
            
        
    
    return len(result)