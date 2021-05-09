#22 括号生成
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def backtrack(path='', left=n, right=n):
            if right < left:
                return
            if left < 0 or right < 0:
                return
            if left == 0 and right == 0:
                res.append(path)
                return

            backtrack(path + '(', left - 1, right)  # 做出选择'('，递归执行，撤销选择
            backtrack(path + ')', left, right - 1)  # 做出选择')'，递归执行，撤销选择

        backtrack()
        return res

#127 单词接龙
class Solution():
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList=set(wordList)
        q=[(beginWord,1)]
        if endWord not in wordList:
            return 0
        while q:
            node,level=q.pop(0)
            if node == endWord:
                return level
            for i in range(len(node)):
                for j in "abcdefghijklmnopqrstuvwxyz":
                    new=node[:i]+j+node[i+1:]
                    if new in wordList:
                        q.append((new,level+1))
                        wordList.remove(new)
        return 0

