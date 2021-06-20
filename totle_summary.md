#### 数组(array) 

删除插入时间空间复杂度

优点：定义简单，访问方便复杂度为O(1)；

缺点：插入和删除会使得元素移动导致速度慢，并且其“内存”大小固定。



#### 链表(link list)

1. 定义结点

结点的数据结构为数据元素(item)与 指针(next)

```python3
class Node(object):
    """单链表的结点"""

    def __init__(self, item):
        # item存放数据元素
        self.item = item
        # next是下一个节点的标识
        self.next = None
```

2. 定义链表

链表需要具有首地址指针head。

```python3
class SingleLinkList(object):
    """单链表"""

    def __init__(self):
        self._head = None
```

示例：创建链表

```python3
if __name__ == '__main__':
    # 创建链表
    link_list = SingleLinkList()
    # 创建结点
    node1 = Node(1)
    node2 = Node(2)

    # 将结点添加到链表
    link_list._head = node1
    # 将第一个结点的next指针指向下一结点
    node1.next = node2

    # 访问链表
    print(link_list._head.item)  # 访问第一个结点数据
    print(link_list._head.next.item)  # 访问第二个结点数据
```

优点：

（1）插入和删除速度快，保留原有的物理顺序，在插入或者删除一个元素的时候，只需要改变指针指向即可。
（2）没有空间限制,存储元素无上限,只与内存空间大小有关. 
（3）动态分配内存空间，不用事先开辟内存
（4)是内存的利用率变高

缺点：

（1）占用额外的空间以存储指针，比较浪费空间，不连续存储)
（2）查找速度比较慢，因为在查找时，需要循环链表。
时间复杂度 :查找操作为O(n) ,插入和删除操作为O(1)。



#### 链表跳表(skip list)

缺点：只能用于元素有序的情况。

优点：原理简单、容易实现、方便扩展、效率更高。



#### 栈（stack）

栈是限定仅在表尾进行插入和删除操作的线性表。这一端被称为栈顶，相对地，把另一端称为栈底。

优点：

 (1)、快速访问。
 (2)、没有必要明确的创建分类变量，因为它是自动管理的。
 (3)、空间被CPU高效地管理着，内存不会变成碎片。

缺点：

 (1)、只有局部变量
 (2)、受限于栈大小(取决于操作系统)
 (3)、变量不能调整大小。

**列表实现的栈类**

```python
class Stack(object):
    # 初始化栈为空列表
    def __init__(self):
        self.items = []
 
    # 判断栈是否为空，返回布尔值
    def is_empty(self):
        return self.items == []
 
    # 返回栈顶元素
    def peek(self):
        return self.items[len(self.items) - 1]
 
    # 返回栈的大小
    def size(self):
        return len(self.items)
 
    # 压栈，入栈，进栈
    def push(self, item):
        self.items.append(item)
 
    # 出栈
    def pop(self):
        return self.items.pop()
```

#### 队列(queue)

```python
class Queue:
    def __init__(self):
        self.items = []

    def push(self, value):  
        self.items.append(value)

    def pop(self):
        return self.items.pop(0)  
```

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

#### 递归

特点：函数自己调用自己

```python
#python模板
def recursion(level, param1, param2, ...): 
	# recursion terminator 
	if level > MAX_LEVEL: 
 		process_result 
 		return 
	# process logic in current level 
	process(level, data...) 
    
	# drill down 
	self.recursion(level + 1, p1, ...) 
    
	# reverse the current level status if needed
```



#### 分治

特点：属于递归，在递归的基础上多了分组和结果合并

```python
def divide_conquer(problem, param1, param2, ...): 
	# recursion terminator 
	if problem is None: 
 		print_result 
 		return 
	# prepare data 
 	data = prepare_data(problem) 
 	subproblems = split_problem(problem, data) 
	# conquer subproblems 
 	subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
 	subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
 	subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
	...
	# process and generate the final result 
 	result = process_result(subresult1, subresult2, subresult3, …) 
 
 	# revert the current level states
```



#### 回溯

回溯法采用试错的思想，它尝试分步的去解决一个问题。在分步解决问题的过程

中，当它通过尝试发现现有的分步答案不能得到有效的正确的解答的时候，它将

取消上一步甚至是上几步的计算，再通过其它的可能的分步解答再次尝试寻找问

题的答案。

回溯法通常用最简单的递归方法来实现，在反复重复上述的步骤后可能出现两种

情况：

• 找到一个可能存在的正确的答案；

• 在尝试了所有可能的分步方法后宣告该问题没有答案。

在最坏的情况下，回溯法会导致一次复杂度为指数时间的计算。

经典例题：八皇后

#### 深度优先搜索与广度优先搜索

搜索 - 遍历

• 每个节点都要访问一次

• 每个节点仅仅要访问一次

• 对于节点的访问顺序不限 

\- 深度优先：depth first search 

\- 广度优先：breadth first search



```python
DFS 代码 - 递归写法
visited = set() 
def dfs(node, visited): 
	if node in visited: # terminator 
		# already visited 
		return 
 	visited.add(node) 
	
    # process current node here. 
	...
	for next_node in node.children(): 
 		if not next_node in visited: 
 			dfs(next node, visited)
```

```python
DFS 代码 - 非递归写法
def DFS(self, tree): 
	if tree.root is None: 
 		return [] 
 	visited, stack = [], [tree.root] 
	while stack: 
 		node = stack.pop() 
 		visited.add(node) 
 		process (node) 
 		nodes = generate_related_nodes(node) 
 		stack.push(nodes) 
	# other processing work 
	...
```

```python
BFS 代码
def BFS(graph, start, end): 
 	queue = [] 
 	queue.append([start]) 
 	visited.add(start) 
	while queue: 
		node = queue.pop() 
 		visited.add(node) 
 		process(node) 
 		nodes = generate_related_nodes(node) 
 		queue.push(nodes)
```

#### 贪心算法 Greedy

贪心算法是一种在每一步选择中都采取在当前状态下最好或最优（即最有

利）的选择，从而希望导致结果是全局最好或最优的算法。



适用贪心算法的场景

简单地说，问题能够分解成子问题来解决，子问题的最优解能递推到最终

问题的最优解。这种子问题最优解称为最优子结构。



#### 二分查找

二分查找的前提

1. 目标函数单调性（单调递增或者递减）

2. 存在上下界（bounded）

3. 能够通过索引访问（index accessible)

```python
left, right = 0, len(array) - 1 
while left <= right: 
	mid = (left + right) / 2 
 	if array[mid] == target: 
 		# find the target!! 
 		break or return result 
 	elif array[mid] < target: 
 		left = mid + 1 
 	else: 
 		right = mid - 1
```

#### 初级搜索

1. 朴素搜索

2. 优化方式：不重复（fibonacci）、剪枝（生成括号问题）

3. 搜索方向：

DFS: depth first search 深度优先搜索

BFS: breadth first search 广度优先搜索

双向搜索、启发式搜索



#### 回溯法

回溯法采用试错的思想，它尝试分步的去解决一个问题。在分步解决问题的过程中，当

它通过尝试发现现有的分步答案不能得到有效的正确的解答的时候，它将取消上一步甚

至是上几步的计算，再通过其它的可能的分步解答再次尝试寻找问题的答案。

回溯法通常用最简单的递归方法来实现，在反复重复上述的步骤后可能出现两种情况： 

• 找到一个可能存在的正确的答案

• 在尝试了所有可能的分步方法后宣告该问题没有答案

在最坏的情况下，回溯法会导致一次复杂度为指数时间的计算。



#### 启发式搜索

估价函数

启发式函数： h(n)，它用来评价哪些结点最有希望的是一个我们要找的

结点，h(n) 会返回一个非负实数,也可以认为是从结点n的目标结点路径的

估计成本。

启发式函数是一种告知搜索方向的方法。它提供了一种明智的方法来猜

测哪个邻居结点会导向一个目标。

#### 字典树

基本结构

字典树，即 Trie 树，又称单词查找树或键树，是一种树形结构。典型应用是用于统计和排序大量的字符串（但不仅限于字符串），所以经常被搜索引擎系统用于文本词频统计。它的优点是：最大限度地减少无谓的字符串比较，查询效率比哈希表高。



基本性质

1. 结点本身不存完整单词；

2. 从根结点到某一结点，路径上经过的字符连接起来，为该结点对应的字符串；

3. 每个结点的所有子结点路径代表的字符都不相同。



核心思想

Trie 树的核心思想是空间换时间。

利用字符串的公共前缀来降低查询时间的开销以达到提高效率的目的。



#### 并查集

基本操作

• makeSet(s)：建立一个新的并查集，其中包含 s 个单元素集合。

• unionSet(x, y)：把元素 x 和元素 y 所在的集合合并，要求 x 和 y 所在的集合不相交，如果相交则不合并。

• find(x)：找到元素 x 所在的集合的代表，该操作也可以用于判断两个元素是否位于同一个集合，只要将它们各自的代表比较一下就可以了。

#### 排序

1. 比较类排序： 通过比较来决定元素间的相对次序，由于其时间复杂度不能突破 O(nlogn)，因此也称为非线性时间比较类排序。
2. 非比较类排序： 不通过比较来决定元素间的相对次序，它可以突破基于比较排序的时 间下界，以线性时间运行，因此也称为线性时间非比较类排序。



#### 初级排序(O(n^2))

1. 选择排序（Selection Sort） 每次找最小值，然后放到待排序数组的起始位置。
2. 插入排序（Insertion Sort） 从前到后逐步构建有序序列；对于未排序数据，在已排序序列中从后 向前扫描，找到相应位置并插入
3. 冒泡排序（Bubble Sort） 嵌套循环，每次查看相邻的元素如果逆序，则交换。



#### 高级排序(O(N*LogN))

- 快速排序（Quick Sort） 数组取标杆 pivot，将小元素放 pivot左边，大元素放右侧，然后依 次对右边和右边的子数组继续快排；以达到整个序列有序。

- 归并排序（Merge Sort）— 分治 1. 把长度为n的输入序列分成两个长度为n/2的子序列； 2. 对这两个子序列分别采用归并排序； 3. 将两个排序好的子序列合并成一个最终的排序序列。
- 堆排序（Heap Sort） — 堆插入 O(logN)，取最大/小值 O(1) 1. 数组元素依次建立小顶堆 2. 依次取堆顶元素，并删除

#### 字符串算法





