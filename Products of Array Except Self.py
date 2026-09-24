import math
class OldSolution:
    #Doesnt work as total_product will always be zero if there exists a single zero in nums
    def OldproductExceptSelf(self, nums: List[int]) -> List[int]:
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

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_cumulative = [1]
        nums_reverse_cumulative = [1]
        
        result = []
        
        nums_reverse = nums.copy()
        nums_reverse.reverse()
        print(nums)
        print(nums_reverse)
        
        for i in range(1, len(nums)):
            nums_cumulative.append(nums_cumulative[i - 1] * nums[i - 1])
            print(nums_cumulative)
        
        for i in range(1, len(nums)):
            nums_reverse_cumulative.append(nums_reverse_cumulative[i-1] * nums_reverse[i-1])
            print(nums_reverse_cumulative)
                
        nums_reverse_cumulative.reverse()
        print("///")
        print(nums_reverse_cumulative)
        print(nums_cumulative)
        #print(len(nums))
        for i in range(0, len(nums) ):
            result.append(nums_cumulative[i] * nums_reverse_cumulative[i])
            print(result[i])
        return result
            
            



sol = Solution()
print(sol.productExceptSelf([1,2,4,6]))