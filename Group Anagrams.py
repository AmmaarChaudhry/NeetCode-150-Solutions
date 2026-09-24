"""
Plan:
Iterate through each string, and break up into a list of chars
find sets for these char lists
Create Hash Map, with the sets as a key, and associated lists of chars as values
Rebuild list of lists

"""
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    dicts = {}
    for word in strs:
        char_list = []
        for char in word:
            char_list.append(char)
        print(char_list)
        char_set = set(char_list)
        if char_set in dicts:
            dicts[char_set] = word
        else:
            dicts.setdefault(char_set, [])
            dicts.append(word)
        
        
    return True
    
    
    
    
    
strs = ["act","pots","tops","cat","stop","hat"]
print(groupAnagrams(strs))
    
