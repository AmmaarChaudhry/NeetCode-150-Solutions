def oldisAnagram(s: str, t: str) -> bool:
    #Inefficient solution:
    if len(s) != len(t):
        return False

    s_list = []
    t_list = []
    
    for char in s:
        s_list.append(char)
        
    for char in t:
        t_list.append(char)
            
    for char in s_list:
        #print(t_list)
        if char in t_list:
            t_list.remove(char)
        else:
            return False
    return True

def isAnagram(s: str, t: str) -> bool:
    #better method, puts all chars from s and t strings into dictionaries and compares them
    if len(s) != len(t):
        return False
    
    s_dict = {}
    t_dict = {}
    
    for char in s:
        if char in s_dict.keys():
            s_dict[char] += 1
        else:
            s_dict.setdefault(char,1)
            
    for char in t:
        if char in t_dict.keys():
            t_dict[char] += 1
        else:
            t_dict.setdefault(char,1)
            
    if s_dict == t_dict:
        return True
    else:
        return False
            
    print(s_dict)
    print(t_dict)
    
    return True
            
    
    
    
    
print(isAnagram("Hello","Hello"))



        