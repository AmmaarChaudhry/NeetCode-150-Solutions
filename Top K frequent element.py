def topKFrequent(nums: List[int], k: int) -> List[int]:
    dicts = {}
    return_list = []
    
    for num in nums:
        if num in dicts:
            dicts[num] += 1
        else:
            dicts.setdefault(num,1)
    #print(dicts)
    #print(max(dicts.values()))
    for i in range(0,k):
        max_key = max(dicts, key = dicts.get)
        #print(max_key)
        return_list.append(max_key)
        del dicts[max_key]
    return return_list
        
    
print(topKFrequent([1,2,2,3,3,3,3],2))




