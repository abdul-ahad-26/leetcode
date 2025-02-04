class Solution:
    def isPowerOf(self, n: int, number: int) -> bool:


        if n==1 : 
            return True
        elif n%number==0:
            return self.isPowerOf(n/number,number)
        else:
            return False
        

s1 = Solution()
print(s1.isPowerOf(25,6))