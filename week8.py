# -*- coding: utf-8 -*-

# 191. 位1的个数
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

# 231. 2 的幂
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n == n & (-n) if n else False

#190. 颠倒二进制位
class Solution:
    def reverseBits(self, n: int) -> int:
        return int('0b'+ bin(n)[2:][::-1] + '0' * (32-len(bin(n)[2:])), 2)

