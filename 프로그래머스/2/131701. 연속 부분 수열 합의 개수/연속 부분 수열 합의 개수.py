from collections import deque

def solution(elements):
    answer = 0
    queue = deque(elements)
    result = set(elements)
    lene = len(elements)
    
    for i in range(lene):
        answer = queue.popleft()
        for j in range(i+1, i+lene):		# j = 7, lene = 5일 때,
            answer += elements[j%lene]		# 12 % 5 = 2로 원형배열 역할을 하게된다.
            result.add(answer)
            
        
    
    return len(result)
