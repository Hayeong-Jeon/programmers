def solution(s):
    answer = 0
    result = True
    lists = list(s)
    stack = []
    
    for i in lists:
        if len(stack) != 0 and stack[-1] == i:   # 스택이 비어있지 않으면서
            stack.pop()							 # 마지막 값이 다음 올 문자와 같다면 pop
        else:
            stack.append(i)						 # 다르다면 다음 올 문자를 push
            
    if len(stack) ==0:							 # 스택이 비어있다면 모두 제거됐으므로 1
        answer = 1
    else:
        answer = 0

    return answer
