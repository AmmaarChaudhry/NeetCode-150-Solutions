#Inefficient method:
def hasDuplicate(nums: List[int]) -> bool:
    check_list = []
    for num in nums:
        if len(check_list) != 0:
            if num in check_list:
                return True
            check_list.append(num)
        check_list.append(num)
    return False



nums = [1,2,3,1]
print(hasDuplicate(nums))