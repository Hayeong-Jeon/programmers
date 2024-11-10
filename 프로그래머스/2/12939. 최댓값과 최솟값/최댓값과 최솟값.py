def solution(s):
    answer=[]
    num1 = [int(i) for i in s.split(' ')]
    answer.append(str(min(num1)))
    answer.append(str(max(num1)))
    
    print(answer)
    
    string =''
    for i in answer:
        string += i + ' '
    
    print(string)
    return string.strip()