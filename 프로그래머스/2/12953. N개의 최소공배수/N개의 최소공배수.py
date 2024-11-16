def solution(arr):
    answer = True
    
    maxn = max(arr)
    
    arr.sort()
    i = 1
    while answer:
        gop = maxn * i
        for j in arr:
            if j == maxn:
                answer = False
                break
            elif gop%j==0:
                continue
            
            else:
                break
        i+=1
        
    return gop