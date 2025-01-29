class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        
        n = len(code) 
        extend_code = code + code
        becrypt = []
        
        if k > 0:
            for i in range(n):
                sum_value = sum(extend_code[i+1 : i+1+k ])
                becrypt.append(sum_value)
        
        elif k < 0:
            for i in range(n):
                sum_value = sum(extend_code[i+n+k : i+n])
                becrypt.append(sum_value)
        
        else:
            becrypt = [0] * n

        return becrypt
