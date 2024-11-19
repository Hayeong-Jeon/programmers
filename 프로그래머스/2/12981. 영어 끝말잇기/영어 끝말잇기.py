def solution(n, words):
    lenw = len(words)
    turn=1
    word = set()
    a =1
    b =1

    for s in range(lenw -1):
        word.add(words[s])
        print(a,b)
        
        if a==n:
            a=1
            b+=1
        else:
            a+=1
        
        if words[s+1] in word or words[s][-1] != words[s+1][0]:
            turn+=s+1
            break


    if turn == 1:
        return [0,0]
    

    return [a,b]