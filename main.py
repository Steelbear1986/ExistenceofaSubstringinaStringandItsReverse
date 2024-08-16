class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        for i in range(len(s)):
            for j in range(len(s) + 1, i + 1, -1):
                if s[i:j] in s[::-1] and len(s[i:j]) >= 2:
                    return True

        return False