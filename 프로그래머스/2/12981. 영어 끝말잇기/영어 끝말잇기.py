def solution(n, words):
    lenw = len(words)
    turn = 1
    word = set()				# 다음 단어의 중복을 찾기위해 집합함수 사용
    a = 1						# a번 째 사람
    b = 1						# b번 째 턴

    for s in range(lenw -1):
        word.add(words[s])		
        
        if a == n:
            a = 1
            b+= 1
        else:
            a+=1
            
        # 다음 단어가 집합함수에 존재한다거나, 끝말잇기가 되지 않는다면 반복문 중지
        if words[s+1] in word or words[s][-1] != words[s+1][0]:
            turn+= s+1		# 다음 턴에 턴이 끝남	
            break


    if turn == 1:			# if 문에 걸리지 않았다면 turn은 변함없음
        return [0,0]
    

    return [a,b]
