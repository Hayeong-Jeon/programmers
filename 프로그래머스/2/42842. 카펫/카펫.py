def solution(brown, yellow):
    answer = []
    total = brown + yellow
    
    #(x-2)*(y-2) = yellow
    #x * y = yellow + brown
    #yellow + brown - 2x - 2y +4 = yellow
    
    #x+y = brown//2 +2
    
    for i in range(3,total+1):
        if total%i ==0:
            y=i
            x=total//i
            if (x-2)*(y-2) == yellow:
                return[x, y]
