def solution(s):
    answer = False
    lens = len(s)
    n = -1
    if s[0]=="(":
        for i in range(lens):
            if s[i]=="(":
                n+=1
            elif s[i]==")":
                n-=1
            if n < -1:
                answer = False
                break
        if n == -1: n = 0
        else:
            return False
    elif s[0]==")" or s[lens-1]!=")":
        answer = False
    
    print("last:", n)
    if n == 0:
        answer = True
    else:
        answer = False
    
    return answer