class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dicts = {}
        sums = []
        return_list = []
        #remove_duplicates = []
        
        for counter in range(0, len(nums)):
            difference = 0 - nums[counter]
            #print(difference)
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

        #print(sums)
        #Removes repeating sets of indexes
        sums_cleaned = []
        for combos in sums:
            if set(combos) not in sums_cleaned:
                sums_cleaned.append(set(combos))
        #print("////")
        #print(sums_cleaned)
        
        #Converts the nested list of indexes into nums values
        for combos in sums_cleaned:
            combos_list = list(combos)
            return_sublist = []
            #print(combos_list[0])
            return_sublist.append(nums[combos_list[0]])
            return_sublist.append(nums[combos_list[1]])
            return_sublist.append(nums[combos_list[2]])
            return_list.append(return_sublist)
       
        #Cleans nested list one more time to remove duplicates:
        #unique = [list(x) for x in {tuple(sorted(x)) for x in lists}]
        return_list_cleaned = [list(x) for x in {tuple(sorted(x)) for x in return_list}]
        print(return_list_cleaned)
        return return_list_cleaned   
        
        
        
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