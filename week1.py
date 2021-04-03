#删除有序数组中的重复项
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        slow = 0
        for quick in range(1, len(nums)):
            if nums[slow] != nums[quick]:
                slow += 1
                nums[slow] = nums[quick]
        return slow + 1

# 旋转数组
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        print(n)
        k %= n
        print(k)
        for _ in range(k):
            nums.insert(0, nums.pop())

# 合并两个有序链表
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        results=[]
        while l1:
            results.append(l1.val)
            l1=l1.next
        while l2:
            results.append(l2.val)
            l2=l2.next
        results.sort()
        head=ListNode()
        dummy=head
        for i in results:
            dummy.next=ListNode(i)
            dummy=dummy.next
        return head.next