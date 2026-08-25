class Solution:
    def isPalindrome(self, x: int) -> bool:
        org = x
        rev = 0
        while x>0:
            digit = x%10
            rev = rev*10+digit
            x = x//10
        if org == rev:
            return True
        else:
            return False

        