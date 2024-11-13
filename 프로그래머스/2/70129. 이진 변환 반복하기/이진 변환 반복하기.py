def solution(s):
    string = s
    sumn = 0									# 없앤 0의 갯수
    count = 0									# 몇 번 반복했는지

    while string != '1':						# string이 '1'이 될 때 까지 반복
        
        sumn += string.count('0')				# string에 있는 '0'의 갯수 카운트
        
        string = bin(string.count('1'))			# '1'의 갯수만큼 센 갯수를 이진수로 변환
        string = string[2:]						# 변환 시'0bxx'로 변환되기에 '0b'없애주기
        
        count += 1								# 총 반복된 횟수

    return [count, sumn]
