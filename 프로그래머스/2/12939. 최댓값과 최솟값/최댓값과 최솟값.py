def solution(s):
    answer=[]
    num = [int(i) for i in s.split(' ')]   #공백을 기준으로 나누어 num에 저장

    answer.append(str(min(num)))   #answer에 num배열 중 가장 큰 값, 작은 값을 문자열로 저장
    answer.append(str(max(num)))

    string =''
    for i in answer:
        string += i + ' '    #string에는 최종적으로 "작은값 큰값 "으로 저장 되기때문에
        					 #마지막에 저장된 공백을 제거하기 위해 .strip()함수를 사용

    return string.strip()
