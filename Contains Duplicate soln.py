#Inefficient method:
def hasDuplicateOld(nums: List[int]) -> bool:
    check_list = []
    for num in nums:
        if len(check_list) != 0:
            if num in check_list:
                return True
            check_list.append(num)
        check_list.append(num)
    return False

def hasDuplicate(nums: List[int]) -> bool:
    #Much more efficient method, compares nums list to nums set. As set can't contain duplicates,
    #this allows us to verify if nums list contains duplicates.
    #This passes NeetCode verification!
    if len(nums) == len(set(nums)):
        return False
    return True


nums = [1,2,3,1]
print(hasDuplicate(nums))