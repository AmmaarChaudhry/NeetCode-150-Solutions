class Solution:
    def isPalindrome(self, s: str) -> bool:
        check_flag = True
        s = s.replace(" ","")
        special_char = ["!","?",".",",", "'", ":", ";", "&", "(", ")"]
        
        for char in special_char:
            s = s.replace(char,"")
        #print(s)
        s_length = len(s) -1
        s = s.lower()
        
        for i in range(0,s_length + 1):
            #print(s[i])
            #print(s[s_length - i])
            print(f"{s[i]} , {s[s_length - i]}")
            if (s[i] != s[s_length - i]):
                return False
            
        return True
        
        
sol = Solution()
print(sol.isPalindrome("tab a cat"))