class Solution:
    def isPalindrome(self, s):
        import re
        s = re.sub(r'[\W_]', '', s).lower()

        # Solution 1
        front = 0
        back = len(s)-1

        while front < back:
            if(s[front] != s[back]):
                return False
            front += 1
            back -= 1
        return True
