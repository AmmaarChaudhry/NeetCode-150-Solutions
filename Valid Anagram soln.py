def isAnagram(s: str, t: str) -> bool:
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
    
    
print(isAnagram("Hello","Hello"))

        