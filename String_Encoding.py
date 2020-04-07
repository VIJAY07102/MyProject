def str_en(s):
    dic = {}
    for i in s:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    st = ''
    for i in s:
        try:
            st += str(i) + str(dic[i])
            if i in dic:
                del dic[i]
            else:
                continue
        except KeyError:
            pass
    return st
    
strring = 'wwwwaaabcccdd'
print(str_en(strring))
