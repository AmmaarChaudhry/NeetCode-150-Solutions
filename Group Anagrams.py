"""
Plan:
Iterate through each string, and break up into a list of chars
find sets for these char lists
Create Hash Map, with the sets as a key, and associated lists of chars as values
Rebuild list of lists

edit: This doesnt work! You can't have a set as a key as it is unhashable.
Also you don't need to break up strings into char lists. You can convert straight
to set.
Also why are you even using sets? You need to care about char freq as you are finding anagrams
New plan:
CCreate a hash map w/ sorted words as keys and anagrams from the list as values
then you can build a list of collected values


"""
def groupAnagramsOld(strs: List[str]) -> List[List[str]]:
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
    
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    dicts = {}
    for word in strs:
        sorted_word = ''.join(sorted(word))
        if sorted_word in dicts:
            #dicts[sorted_word] +=1
            dicts[sorted_word].append(word)
        else:
            #dicts.setdefault(sorted_word,1)
            dicts.setdefault(sorted_word,[word])

    sorted_anagrams = dicts.values()
    return list(sorted_anagrams)

        
    
    
    
    
    
strs = ["act","pots","tops","cat","stop","hat"]
print(groupAnagrams(strs))
    
