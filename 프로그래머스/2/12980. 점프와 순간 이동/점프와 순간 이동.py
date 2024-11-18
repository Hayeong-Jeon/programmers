def solution(n):
    
    count = 0
    
    while n>0 :
        if n % 2 == 0:
            n = n//2
            continue
        
        else : n -= 1
        
        count += 1
    
    return count