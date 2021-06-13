#### AVL树

1. 平衡二叉搜索树 
2. 每个结点存 balance factor = {-1, 0, 1}
3. 四种旋转操作 AVL 总结 
4. 不足：结点需要存储额外信息、且调整次数频繁



#### 红黑树

红黑树是一种近似平衡的二叉搜索树（Binary Search Tree），它能够确保任何一 个结点的左右子树的高度差小于两倍。具体来说，红黑树是满足如下条件的二叉 搜索树： 

• 每个结点要么是红色，要么是黑色 

• 根结点是黑色 

• 每个叶结点（NIL结点，空结点）是黑色的。

• 不能有相邻接的两个红色结点 

• 从任一结点到其每个叶子的所有路径都包含相同数目的黑色结点。



#### 对比

• AVL trees providefaster lookups than Red Black Trees because they are more strictly  balanced. 

• Red Black Trees providefaster insertion and removal operations than AVL trees as  fewer rotations are done due to relatively relaxed balancing. 

• AVL trees storebalance factors or heightswith each node, thus requires storage for  an integer per node whereas Red Black Tree requires only 1 bit of information per  node. 

• Red Black Trees are used in most of the language libraries  likemap, multimap, multisetin C++whereas AVL trees are used indatabaseswhere  faster retrievals are required.