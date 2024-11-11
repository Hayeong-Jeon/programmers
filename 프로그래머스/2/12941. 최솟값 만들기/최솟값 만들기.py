def solution(A,B):
    lens = len(A)
    sumAB = 0
    
    A.sort(reverse=True)  		#내림차순 정렬
    B.sort()			  		#오름차순 정렬
    
    for i in range(lens):		
        sumAB += A[i] * B[i]

    return sumAB
