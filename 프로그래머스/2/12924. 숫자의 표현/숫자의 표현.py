def solution(n):
    count = 0
    
    for i in range(1,n+1):			# 1 ~ n까지 증가하도록
        sumn = 0
        j = i
        for k in range(j,n+1):		# k는 1 ~ n, 2 ~ n ... n (연속된 숫자)
            sumn += k				# 연속된 숫자들을 더하면서 n이 되는지 판단
            
            if sumn == n :			# n이 되는 연속된 숫자의 합이 있다면 count++
                count += 1
            elif sumn >= n:			# 합이 n을 넘어가면 중지
                break
    
    return count
