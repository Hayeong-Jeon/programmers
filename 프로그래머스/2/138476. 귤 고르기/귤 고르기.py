from collections import Counter
def solution(k, tangerine):

    a = Counter(tangerine)
    n=0
    
    for item, count in a.most_common():	 # 가장 많은 요소 기준으로 정렬
        k -= count
        n += 1
        
        if k <= 0 :
            break
        
    return n
