class Solution:
    def isPowerOfFour(self, n: int) -> bool:


        if n==1 : 
            return True
        elif n%4==0:
            return self.isPowerOfFour(n/4)
        else:
            return False
        

s1 = Solution()
print(s1.isPowerOfFour(16))