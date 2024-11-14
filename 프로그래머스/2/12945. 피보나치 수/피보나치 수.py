def solution(n):
    answer = True
    count=2
    bef = 0
    aft = 1
    sumn=bef+aft
    result=0
    
    while answer:
        if count == n:
            result=sumn%1234567
            answer = False
            continue
        bef=aft
        aft=sumn
        sumn=bef+aft
        count+=1
        
    return result
