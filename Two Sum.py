def twoSum(nums: List[int], target: int) -> List[int]:
    dictionary = {}
    for i in range(0, len(nums)):
        difference = target - nums[i]
        dictionary[difference] = i
    print(dictionary)
    
    for j in range(0, len(nums)):
        if nums[j] in dictionary:
            return_i = dictionary.get(nums[j])
            if(return_i<j):
                return[return_i,j]
            else:
                return[j,return_i]
    
    
        

nums = [3,4,5,6]
target = 7

print(twoSum(nums,target))

class Solution:
    def twoSum(nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i in range(0, len(nums)):
            difference = target - nums[i]
            dictionary[difference] = i
        print(dictionary)
        
        for j in range(0, len(nums)):
            if nums[j] in dictionary:
                return_i = dictionary.get(nums[j])
                if(return_i<j):
                    return[return_i,j]
                else:
                    return[j,return_i]

        