#236. 二叉树的最近公共祖先
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        # 边界条件，如果匹配到left或right就直接返回停止递归
        if root.val == p.val or root.val == q.val:
            return root
        # 这两行代码可以无脑先写好！
        # 因为是DFS算法，这个模板可以无脑套用，写上之后可能你思路就清晰很多
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # 如果既在左子树找到，又在右子树找到，那么毫无疑问当前root就是公共节点
        if left and right:
            return root
        # 只有左子树有，那么直接返回左子树匹配到的第一个节点
        if left:
            return left
        if right:
            return right

#105. 从前序与中序遍历序列构造二叉树
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None
        # 前序遍历第一个值为根节点
        root = TreeNode(preorder[0])
        # 因为没有重复元素，所以可以直接根据值来查找根节点在中序遍历中的位置
        mid = inorder.index(preorder[0])
        # 构建左子树
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        # 构建右子树
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root

#77. 组合
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrace(i,tmp):
            if len(tmp) == k:
                res.append(tmp)
                return
            for j in range(i,n+1):
                backtrace(j+1,tmp+[j])
        backtrace(1,[])
        return res
