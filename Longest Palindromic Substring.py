class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        if len(s) == 1:
            return s
        if s[::-1] == s:
            return s
        for i in range(len(s)):
            try:
                characterIndexs = [_ for _ in range(len(s)) if s[_] == s[i] and _ > i]
                for index in characterIndexs:
                    if s[i:index+1] == s[i:index+1][::-1] and len(s[i:index+1]) > len(longest):
                        longest = s[i:index+1]
            except:
                pass
        if longest == "":
                return s[0]
        return longest