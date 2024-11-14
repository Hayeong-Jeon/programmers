def solution(n):
    answer = True
    nextn = n+1
    while answer:
        if bin(n).count('1') == bin(nextn).count('1'): # 이진수 변환 후 '1'의 갯수 같은지
            answer = False
            continue
    
        nextn+=1       # 아니라면 다음 수 증가
    return nextn
