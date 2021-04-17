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