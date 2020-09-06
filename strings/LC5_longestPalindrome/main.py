# Given a string s, find the longest palindromic substring in s
# --- Example
# longestPalindrome("cbbd") --> "bb"
# longestPalindrome("abba") --> "abba"
# longestPalindrome("a") --> "a"

class Solution:
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            # print("for", i, ": ")
            current = self.findS(s, i-1, i+1)
            in_bet = self.findS(s, i, i+1)
            res = max(res, current, in_bet, key=len)
            # print("current", current, " in_bet:", in_bet, " res", res)
        return res

    def findS(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]


# obj = Solution()
# s = "madam"
# print("final:"+obj.longestPalindrome(s))
