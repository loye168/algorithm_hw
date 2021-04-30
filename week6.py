#64. 最小路径和
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        f = grid
        for i in range(1, m):
            f[i][0] += f[i-1][0]
        for j in range(1, n):
            f[0][j] += f[0][j-1]

        for i in range(1, m):
            for j in range(1, n):
                f[i][j] += min(f[i-1][j], f[i][j-1])
        return f[m-1][n-1]

#91. 解码方法
class Solution:
    def numDecodings(self, s: str) -> int:

        if s[0] == "0":
            return 0

        n = len(s)
        dp = [1] * n

        for i in range(1, n):

            if s[i] == "0":
                if s[i - 1] in ["1", "2"]:
                    dp[i] = dp[i - 2]
                else:
                    return 0
            elif s[i - 1] == "1" or s[i - 1] == "2" and 1 <= int(s[i]) <= 6:
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]

        return dp[-1]

#221. 最大正方形
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix)==0:
            return 0
        def exc(l):
            return list(map(int,l))
        dp=list(map(exc,matrix))
        a,b=len(matrix[0]),len(matrix)
        for i in range(1,b):
            for j in range(1,a):
                if dp[i][j]==1:
                    dp[i][j]=min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+1
        return max(list(map(max,dp)))**2221