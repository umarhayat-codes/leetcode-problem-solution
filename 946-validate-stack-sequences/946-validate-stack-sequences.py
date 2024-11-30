class Solution:
    def validateStackSequences(self,pushed,popped):
        stack = []
        i = 0
        for val in pushed:
            stack.append(val)
            while stack and i < len(pushed) and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return len(stack) == 0

obj = Solution()
print(obj.validateStackSequences([1,2,3,4,5],[4,5,3,2,1]))

