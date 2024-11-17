def solution(arr):
    answer = True
    maxn = max(arr)
    arr.sort()						# maxn의 값을 맨 뒤로 보내기 위함
    i = 1
    
    while answer:
        gop = maxn * i
        
        for j in arr:
            if j == maxn:		   # maxn에 도달했을 때, 모든 arr의 값이 gop의 약수이며
                answer = False	   # 해당 gop이 최소공배수 일 것이므로 반복문 중지
                break
            elif gop % j == 0:
                continue
            
            else:
                break
        i+=1
        
    return gop
