#242. 有效的字母异位词
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = Counter(s)
        t_dict = Counter(t)
        return s_dict == t_dict

#1. 两数之和
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for ind,num in enumerate(nums):
            hashmap[num] = ind
        for i,num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None and i!=j:
                return [i,j]

#589. N 叉树的前序遍历
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        #前序遍历
        def pre_order(root):
            #跟节点非空入队列递归遍历
            if root:
                #节点值入队列
                result.append(root.val)
                #递归遍历
                for node in root.children:
                    pre_order(node)
        pre_order(root)
        return result

#49. 字母异位词分组
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            key = tuple(sorted(s))
            if key not in dic:
                dic[key] = [s]
            else:
                dic[key].append(s)
        return list(dic.values())

#347. 前 K 个高频元素
#哈希表+使用小顶堆代替大顶堆
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num] = 1
        heap=[]
        for i in set(nums):
            heapq.heappush(heap, (-hashmap[i],i))
        res=[]
        i=1
        while i<=k:
            _, ans = heapq.heappop(heap)
            res.append(ans)
            i+=1
        return res