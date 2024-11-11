def solution(s):
    answer = False
    lens = len(s)
    n = -1
    if s[0]=="(":						#'('로 시작하는 문자열만 해당하도록
        
        for i in range(lens):			
            if s[i]=="(":
                n+=1
            elif s[i]==")":
                n-=1
            if n < -1:					#'())(()' 이렇게 나오는 것을 방지
                answer = False
                break
                
        if n == -1: 					#n이 초기값 그대로면 '()'로 짝지어졌단 의미
            n = 0						
        else:							#아니라면 짝지어 지지 않았기 때문에 false출력
            return False
        
    elif s[0]==")" or s[lens-1]!=")": 	#')'로 시작하거나'('로 끝나면 false출력
        answer = False

    if n == 0:
        answer = True
    else:
        answer = False
    
    return answer
