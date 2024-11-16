def solution(brown, yellow):

    total = brown + yellow
    
    # 노란색 격자는 갈색 x, y보다 2가 적다는 성질을 이용해서 식을 만들 수 있다.
    # (x-2)*(y-2) = yellow 를 전개해서
    # x * y = yellow + brown 를 대입하면
    # yellow + brown - 2x - 2y +4 = yellow 라는 식이 나오는 데, 정리하면
    # x+y = brown//2 +2 이 식을 사용
    
    for i in range(3,total+1):			# x값은 항상 3이상
        if total%i ==0:     			
            y=i
            x=total//i
            if x+y == (brown//2 +2):	# 이 식을 만족해야만 하나의 x, y가 도출됨
                return[x, y]
