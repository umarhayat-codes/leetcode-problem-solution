class Solution:
    def makeGood(self,s):
        stack = []
        for var in s:
            if stack and stack[-1] != var and stack[-1].lower() == var.lower():
                stack.pop()
            else:
                stack.append(var)
        return "".join(stack)

obj = Solution()
print(obj.makeGood("abBAcC")) 


 
