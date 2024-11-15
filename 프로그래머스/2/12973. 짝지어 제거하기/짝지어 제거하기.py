def solution(s):
    answer = 0
    result = True
    lists = list(s)
    stack = []
    

    for i in lists:
        if len(stack) != 0 and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
            
    if len(stack) ==0:
        answer = 1
    else:
        answer = 0

    return answer