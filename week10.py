# -*- coding: utf-8 -*-
# 8. 字符串转换整数 (atoi)
class Solution:
    def myAtoi(self, str: str) -> int:
        import re
        re_str = r"\s*[-|+]?\d+"
        result = re.match(re_str, str)
        try:
            result = int(result[0].strip(" "))
        except:
            return 0
        else:
            return max(min(result, 2**31 - 1), (-2)**31)

# 438. 找到字符串中所有字母异位词
import collections
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left, right = 0, len(p)
        res = []
        maxLen = len(s)
        s += ' '* len(p)
        window = collections.Counter(s[left:right])
        cnt = collections.Counter(p)
        while left < maxLen:
            if window & cnt == cnt:
                res.append(left)

            window[s[right]] += 1
            window[s[left]] -= 1
            right += 1
            left += 1
        return res

#5. 最长回文子串
class Solution:
    def longestPalindrome(self, s):
        ln = len(s)
        # s为空或者s为自己本身的情况
        if ln < 2:
            return s
        ret = ''

        def finder(left, right):
            nonlocal ret
            while left >= 0 and right < ln and s[left] == s[right]:
                left -= 1
                right += 1
            ret = s[left + 1:right] if right - left - 1 > len(ret) else ret

        for i in range(ln ):
            finder(i, i)
            finder(i, i + 1)
        return ret
