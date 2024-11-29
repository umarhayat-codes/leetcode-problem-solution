class Solution:
    def isValid(self,s):
        start = "({["
        end = ")}]"
        stack = []
        for i in s:
            if i in start:
                stack.append(i)
            else:
                if stack and stack[-1] == start[end.index(i)]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
    
obj = Solution()
print(obj.isValid("()[]{}"))
