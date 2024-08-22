def mysplit(strng):
    
    word = ""
    string_list = []
    count = 0
    
    for ch in strng:

        if ch == ' ' and count == 0:
            continue
        
        if ch != ' ':
            word += ch
            count += 1
        elif ch == ' ':
            string_list.append(word)
            word = ""
            
    if word != ' ' and word != '':        
        string_list.append(word)
    
    return string_list


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit("")) 
