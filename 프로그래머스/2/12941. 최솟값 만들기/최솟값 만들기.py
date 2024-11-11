def solution(A,B):
    answer = 0
    lens = len(A)

    A.sort(reverse=True)  		#내림차순 정렬
    B.sort()			  		#오름차순 정렬
    
    sumAB=0
    
    for i in range(lens):		
        sumAB+=A[i] * B[i]

    return sumAB
