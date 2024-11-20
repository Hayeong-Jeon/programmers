from collections import Counter
def solution(k, tangerine):

    a = Counter(tangerine)
    n=0
    cnt = 0
    
    for item, count in a.most_common():
        k -= count
        n += 1
        
        if k <= 0 :
            break
        
    return n