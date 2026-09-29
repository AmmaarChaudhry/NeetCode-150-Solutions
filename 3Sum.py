class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dicts = {}
        sums = []
        #remove_duplicates = []
        
        for counter in range(0, len(nums)):
            difference = 0 - nums[counter]
            print(difference)
            if difference not in dicts:
                dicts.setdefault(difference, [])
                dicts[difference] = [counter]
            else:
                dicts[difference].append(counter)
        print(dicts)
        
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                #if i != j:
                if i < j:
                    temp_sum = nums[i] + nums[j]
                    if temp_sum in dicts:
                        nums_indexes = dicts.get(temp_sum)
                        if i in nums_indexes:
                            nums_indexes.remove(i)
                        if j in nums_indexes:
                            nums_indexes.remove(j)
                        
                        if nums_indexes != []:
                            for index in nums_indexes:
                                sums.append([index, i, j])
                                #sums.append([   nums[index], nums[i], nums[j]  ])
                            #print(f"{nums_indexes} + {nums[i]} + {nums[j]}")
                        #sums.append([nums[i], nums[j], ])

        print(sums)
        sums_cleaned = []
        for combos in sums:
            if set(combos) not in sums_cleaned:
                sums_cleaned.append(set(combos))
        print("////")
        print(sums_cleaned)
        
        """
        
        for checker in range (0,len(sums)):
            for checker2 in range (0,len(sums)):
                if set(sums[checker]) == set(sums[checker2]) and checker != checker2:
                    remove_duplicates.append(sums[checker])
        
        #print(remove_duplicates)
        for remove in remove_duplicates:
            if remove in sums:     
                sums.remove(remove)
        #print(sums)
        """
        
        
        
sol = Solution()
sol.threeSum([-1,0,1,2,-1,-4])