def solution(A,B):
    answer = 0
    lens = len(A)

    A.sort(reverse=True)
    B.sort()
    
    sumAB=0
    
    for i in range(lens):
        sumAB+=A[i] * B[i]
    
    print(A)
    print(B)

    return sumAB