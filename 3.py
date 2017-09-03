class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        longest = 0
        chars = {}
        for i in xrange(len(s)):
            if chars.has_key(s[i]):
                start = max(start, chars[s[i]] + 1)
            chars[s[i]] = i
            longest = max(longest, i - start + 1)
        return longest