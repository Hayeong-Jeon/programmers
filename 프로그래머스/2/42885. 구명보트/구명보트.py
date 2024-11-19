from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()				# 올림차순 정렬
    queue = deque(people)		# people배열 큐 삽입
    
    while queue:				
        if len(queue) == 1:		# 만약 태울사람이 한명만 남는다면 구명보트 사용
            queue.pop()			# 큐 오른쪽 값 제거
            answer+=1
        
        # 작은 값 + 큰 값 <= 무게제한 일때, 두명 다 태움(큐 양쪽 값 제거)
        elif queue[0] + queue[-1] <= limit:	
            queue.popleft()		
            queue.pop()
            answer+=1
            
       	else:					# 무게제한 넘어갈 시 무거운사람 태움(큐 오른쪽 값 제거)
        	queue.pop()
        	answer+=1
        
        
        
    return answer
