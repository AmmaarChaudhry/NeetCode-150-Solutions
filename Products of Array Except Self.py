import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_list = []
        total_product = math.prod(nums)
        #print(total_product)
        for i in range(0,len(nums)):
            product_list.append(total_product)
            
        #print(product_list)
        #print(nums)
        for j in range(1,len(nums)):
            #print(temp)
            if nums[j] != 0:
                product_list[j] = int(total_product / nums[j])
            else:
                product_list[j] = 0
            #print(f"product_list[j]: {product_list[j]}")
            
        
        return product_list            
            



sol = Solution()
print(sol.productExceptSelf([1,2,4,6]))