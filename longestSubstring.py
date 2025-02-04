class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength = 0
        nonRepeated = []
        maxLength = 0
        if len(s) == 1:
            return 1

        for i in range(len(s)):
            for j in range(i,len(s)):
                
                if s[j] not in nonRepeated:
                    nonRepeated.append(s[j])
                else : 
                    if(maxLength < len(nonRepeated)):
                        maxLength = len(nonRepeated)
                        nonRepeated = []
                        break
                    
        return maxLength
    
obj1 = Solution()
print(obj1.lengthOfLongestSubstring('abcabc'))