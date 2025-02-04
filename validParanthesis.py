class Solution:
    def isValid(self, s: str) -> bool:
        closingBrackets={
            ')':'(',
            ']':'[',
            '}':'{'
        }
        stack=[]

        for c in s:
            if c in closingBrackets:
                if stack and stack[-1] ==  closingBrackets.get(c):
                    stack.pop()
                else: 
                    return False
                
            else:
                stack.append(c)

        if not stack :
            return True
        else:
            return False
        # return True if not stack else False

                

                
            
s = Solution()
print(s.isValid("(){}[]"))


            
        