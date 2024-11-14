def solution(n):
    answer = True
    bef = 0							# n - 2 값
    aft = 1							# n - 1 값
    sumn = bef + aft
    count = 2						# sumn은 2번 째 값이기 때문에
    result = 0
    
    while answer:
        if count == n:				
            result = sumn%1234567
            answer = False
            continue
        bef = aft					# 현재가 n 번 째가 아니라면 한 칸씩 옮긴다
        aft = sumn
        sumn = bef + aft			# n = (n-2 + n-1)
        
        count+=1
        
    return result
