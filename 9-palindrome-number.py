# Palindrome Number	https://leetcode.com/problems/palindrome-number

### Python
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        
        what about if x is 0?
        what about if x is negative?        
        
        x = str(x)
        left = 0
        right = len(x) - 1
        
        while left <= right:
            if x[left] != x[right]:
                return False
            left += 1
            right -= 1
        return True
            
        """        
        
        
        # converting to string and using 2 pointers and index to compare each index.
        
        # O(n) time
        # O(1) space
        
        integer_string = str(x)
        left = 0
        right = len(integer_string) - 1
        
        while left <= right:
            if integer_string[left] != integer_string[right]:
                return False
            # move index +1 and -1:
            left+=1
            right-=1
        return True
        

        
