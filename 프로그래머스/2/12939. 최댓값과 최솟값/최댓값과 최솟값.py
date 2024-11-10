def solution(s):
    answer= []
    num = [int(i) for i in s.split(' ')]

    answer.append(str(min(num)))
    answer.append(str(max(num)))

    string =''
    for i in answer:
        string += i + ' '
    
    return string.strip()