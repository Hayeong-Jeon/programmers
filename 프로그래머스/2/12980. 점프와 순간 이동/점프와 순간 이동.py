from collections import deque

def solution(n):
    queue = deque([(0, 0)])				# 큐를 사용해서 (현재거리, 이동거리) 저장
    visit = set()						# set() 집합함수를 사용하여 방문했던 곳 표시
    visit.add(0)

    while queue:
        cell, dis = queue.popleft()


        if cell == n:
            return dis

        if cell * 2 not in visit:  		   # 순간이동 했을 때, 아직 방문하지 않은 곳이라면
            visit.add(cell * 2)			   # 순간이동해서 방문
            queue.append((cell * 2, dis)) 

        if cell + 1 not in visit and cell + 1 <= n:  # 점프해서 방문
            visit.add(cell + 1)
            queue.append((cell + 1, dis + 1)) 


#    def solution(n):
#    
#        count = 0
#    
#        while n>0 :
#            if n % 2 == 0:
#                n = n // 2
#                continue
#            else:
#                n -=1
#                count+=1
#   
#        return count
