def solution(n,a,b):
    answer = 0
    c=0
    maxn = bin(n).count('0') - 1		 # 최대 라운드 ex) n = 4 = 100 이므로 2라운드
										 # bin() 해주면 0b100로 변환되기 때문에 -1    
    if a > b:							 # a가 b보다 커질 수 있음을 방지
        a, b = b, a
        
    n = n//2                             # 중간을 기준으로 판별
    c = n
    for i in range(maxn, 0, -1):
        if i == 1:
            return 1
        
        if (a > n and b > n):			 # 둘 다 n보다 크면 중간으로 나눈뒤 라운드 -1
            c=c//2
            n += c
            continue
            
        elif (a <=n and b<=n):			 # 적으면 반으로 나눔
            c=c//2
            n -= c
            continue
        return i
