def solution(n):
    answer = 0
    r=[]
    c=0
    for i in range(1,n+1):
        s=0
        j=i
        for k in range(j,n+1):
            s+=k
            r.append(s)
            if s==n :
                c+=1
            elif s>n: break
    return c