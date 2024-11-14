def solution(n):
    answer = True
    nextn = n+1
    while answer:
        
        if bin(n).count('1') == bin(nextn).count('1'):
            answer = False
            continue
    
        nextn+=1
    return nextn