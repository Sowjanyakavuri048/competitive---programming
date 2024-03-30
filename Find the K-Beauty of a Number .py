class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
            num_str = str(num)
            num_str.strip("0")
        
            n = len(num_str)
            result = 0
            for i in range(k - 1, n):
                div = int(num_str[i-k+1:i+1])
                if div != 0 and num % div == 0:
                    result += 1
                    
            return result
