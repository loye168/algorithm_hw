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



#### 其他

五毒法加国际站，过遍数，最大的误区是做题只作一遍，优化的时间升维，一维换二维

懵逼的时候 暴力？基本情况？ 找最近重复子问题



#### 课程所提到题目

移动0（双指针）

柱子最大面积（双指针）

反转链表

判断链表是否有环

有效括号（栈）

最小栈

柱状图中最大矩形（栈）