def solution(s):
    answer = ''
    lens = len(s)
    string = s.title()						#문자열의 첫 글자마다 대문자로 변환
    string = list(string)					#문자열을 리스트로 변환
        
    for i in range(lens):
        if string[i] == " ":				#문자열에 공백이 있다면 넘어감
            continue
        elif string[i].isdigit:				#해당 문자가 숫자면
            if i < lens -1:					#길이 체크해주고 숫자 뒤 문자를 소문자로변환
                string[i+1] = string[i+1].lower()

    answer = ''.join(string)				#리스트를 문자열로 변환
    
    return answer
