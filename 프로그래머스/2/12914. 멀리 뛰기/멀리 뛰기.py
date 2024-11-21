def solution(n):
    answer = 0
    dp = [0] * (n+1)		# n+1 갯수만큼 초기화
    dp[0] = 1				# 0번째 칸 가는 경우의 수 = 제자리 = 1
    dp[1] = 1				# 1번째 칸 가는 경우의 수 = 1칸 점프 = 1
    
    for i in range(2, n+1):
        dp[i] = dp[i-2] + dp[i-1]
        
    
    
    return dp[n] % 1234567
