def solution(n,a,b):
    answer = 0
    
    if a > b:
        a, b = b, a

    while 1:  # 참가자 수가 1보다 클 때까지 반복
        answer += 1  # 라운드 수 증가

        # A와 B가 같은 매치에 있는지 확인
        if (a + 1) // 2 == (b + 1) // 2:
            return answer
    
        # 다음 라운드로 진행
        a = (a + 1) // 2  # A의 번호 업데이트
        b = (b + 1) // 2  # B의 번호 업데이트