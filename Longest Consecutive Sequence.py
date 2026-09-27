class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set = set(nums)
        start_of_seq = []
        longest_seq_length = 0
        current_seq_length = 0
        
        if (num_set == {0}):
            return 1
        if(len(num_set) == 0):
            return 0
        
 
        for i in num_set:
            consec_upper = i + 1
            consec_down = i - 1
            if consec_upper in num_set and consec_down not in num_set:
                #print(i)
                start_of_seq.append(i)
                
                
        print(start_of_seq)
        for j in start_of_seq:
            consec_upper = j
            
            while consec_upper in num_set:
                consec_upper = consec_upper + 1
                current_seq_length = current_seq_length + 1
                
            
            if current_seq_length > longest_seq_length:
                longest_seq_length = current_seq_length
                
            current_seq_length = 0
            
        if longest_seq_length > 1:
            return longest_seq_length
        else:
            return 1
        #return longest_seq_length
            

sol = Solution()
print(sol.longestConsecutive([0,0]))