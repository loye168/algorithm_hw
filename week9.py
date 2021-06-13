# -*- coding: utf-8 -*-

# 1122. 数组的相对排序
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        return sorted(arr1, key=lambda x: (0, arr2.index(x)) if x in arr2 else (1, x))

# 151. 翻转字符串里的单词
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([i for i in s.strip().split(' ') if i][::-1])

# 205. 同构字符串
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return [*map(s.index, s)] == [*map(t.index, t)]
