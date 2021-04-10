#### 哈希表（Hash table）

哈希表也叫散列表，是根据关键码值（Key value ）而直接进行访问的数据结构。 它通过把关键码值映射到表中一个位置来访问记录，以加快查找的 速度。 这个映射函数叫作散列函数（Hash Function），存放记录的数组叫 作哈希表（或散列表）。

在Python中以字典的形式展现

例题：两数之和

```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map_a = dict()
        k = len(nums)
        for i in range(0, k):   #一边将列表中的数添加到字典中，一边判断两数之差是否存在于字典中
            temp = target - nums[i]  
            if temp in map_a :  # 判断步骤
                return [map_a[temp], i]
            map_a[nums[i]] =  i  # 添加步骤（切记先判断再添加，以免key冲突）
```

#### 树(Tree)

**树**是一种数据结构，它是由*n(n>=1*)个有限结点组成一个具有层次关系的集合。

Linked List 是特殊化的 Tree ,Tree 是特殊化的 Graph



#### 二叉树(Binary Tree)

二叉树是n个有限元素的集合，该集合或者为空、或者由一个称为根（root）的元素及两个不相交的、被分别称为左子树和右子树的二叉树组成，是有序树。当集合为空时，称该二叉树为空二叉树。在二叉树中，一个元素也称作一个结点

遍历方式：1.前序（Pre-order）：根-左-右 2.中序（In-order）：左-根-右 3.后序（Post-order）：左-右-根

```python
# 二叉树类
class BTree(object):

    # 初始化
    def __init__(self, data=None, left=None, right=None):
        self.data = data    # 数据域
        self.left = left    # 左子树
        self.right = right  # 右子树
        self.dot = Digraph(comment='Binary Tree')

    # 前序遍历
    def preorder(self):

        if self.data is not None:
            print(self.data, end=' ')
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()

    # 中序遍历
    def inorder(self):

        if self.left is not None:
            self.left.inorder()
        if self.data is not None:
            print(self.data, end=' ')
        if self.right is not None:
            self.right.inorder()

    # 后序遍历
    def postorder(self):

        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        if self.data is not None:
            print(self.data, end=' ')
```



#### 二叉搜索树(Binary Search Tree)

二叉搜索树，也称二叉排序树、有序二叉树（Ordered Binary Tree）、排 序二叉树（Sorted Binary Tree），是指一棵空树或者具有下列性质的二叉 树： 1. 左子树上所有结点的值均小于它的根结点的值； 2. 右子树上所有结点的值均大于它的根结点的值； 3. 以此类推：左、右子树也分别为二叉查找树。 （这就是 重复性！） 中序遍历：升序排列

```python
class BinaryTree:
    def __init__(self):
        self.tree = EmptyNode()
 
    def __repr__(self):
        return repr(self.tree)
 
    def lookup(self, value):
        return self.tree.lookup(value)
 
    def insert(self, value):
        self.tree = self.tree.insert(value)
 
 
class EmptyNode:
    def __repr__(self):
        return '*'
 
    def lookup(self, value):                      # fail at the bottom
        return False
 
    def insert(self, value):
        return BinaryNode(self, value, self)      # add new node at bottom
 
 
class BinaryNode:
    def __init__(self, left, value, right):
        self.data, self.left, self.right  =  value, left, right
 
    def lookup(self, value):
        if self.data == value:
            return True
        elif self.data > value:
            return self.left.lookup(value)               # look in left
        else:
            return self.right.lookup(value)              # look in right
 
    def insert(self, value):
        if self.data > value:
            self.left = self.left.insert(value)          # grow in left
        elif self.data < value:
            self.right = self.right.insert(value)        # grow in right
        return self
 
    def __repr__(self):
        return ('( %s, %s, %s )' %
                 (repr(self.left), repr(self.data), repr(self.right)))
```

#### 堆(Heap)

Heap:可以迅速找到一堆树中的最大或者最小值的数据结构。

将根节点最大的堆叫做大顶堆或者大根堆，根节点最小的堆叫做小顶堆或小根堆。常见的堆有二叉堆、斐波那契堆等。

假设是大顶堆，常见操作(API):

find-max:O(1)

delete-max:O(log N)

insert(create):O(logN) or O(1)



#### 二叉堆(binary Tree)

通过完全二叉树来实现

二叉堆（大顶）它满足下列性质：

①是一个完全树。

②树中任意节点的值总是>=其子节点的值。



实现细节

1、二叉堆一般都是通过“数组”来实现

2、假设“第一个元素”在数组中的索引为0，则父节点和子节点的位置关系如下：

①索引为i的左孩子的索引是(2*i+1)

②索引为i的右孩子的索引是(2*i+2)

③索引为i的父节点的索引是floor((i-1)/2)

常见操作：insert, delete

```python
from pythonds.trees.binheap import BinHeap

bh = BinHeap()
bh.insert(5)
bh.insert(7)
bh.insert(3)
bh.insert(11)

print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
```

