def solution(s):  # "  for the what  1what  "
    answer = ''
    lens = len(s)
    print(lens)
    string = [i for i in s.split(" ")]
    s = s.title()
    s_list = list(s)
        
    for i in range(lens):
        if s[i] == " ":
            continue
        elif s[i].isdigit:
            if i < lens -1:
                s_list[i+1]=s_list[i+1].lower()
            
    print(s_list)
    s=''.join(s_list)
    print(s_list)
    print(s)
    
    return s