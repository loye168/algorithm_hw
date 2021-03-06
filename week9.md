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

