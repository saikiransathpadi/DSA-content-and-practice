class Solution:
    def myPow2(self, x: float, n: int) -> float:

        ans = 1
        ori = n
        n = abs(n)
        while n:
            if n%2 == 1:
                ans *= x 
                n-=1
            else:
                x *= x
                n = n//2
            
        return ans if ori > 0 else 1/ans
    
    def myPow(self, x: float, n: int) -> float:
        return x**n

print("ansss",Solution().myPow2(2,10))
print(Solution().myPow2(2.1,3))
print(Solution().myPow2(2,-2))
# divide and conquer / bin manipulation just - Revisit