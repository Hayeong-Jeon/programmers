def solution(s):
    string = s
    sumn=0
    count=0


    while string != '1':
        
        sumn+=string.count('0')
        
        string=bin(string.count('1'))
        string = string[2:]
        
        count+=1

    return [count, sumn]


#def solution(s):
#    cnt, zero = 0, 0
#    while s != '1' :
#        zero += s.count('0')
#        s = bin(s.count('1'))[2:]
#        cnt+=1

#    return [cnt, zero]