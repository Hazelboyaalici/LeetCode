class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >=0 :
            x1= str(x)
            return x1 ==x1[::-1]

        else:
            return False

