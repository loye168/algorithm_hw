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

