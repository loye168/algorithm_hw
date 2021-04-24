#860. 柠檬水找零
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            dic[bill] += 1
            if bill - 5 == 15:
                if dic[10] >= 1:
                    dic[5] -= 1
                    dic[10] -= 1
                else:
                    dic[5] -= 3
            elif bill - 5 == 5:
                dic[5] -= 1
            else:
                continue
            if dic[5] < 0:
                return False
        return True

#122. 买卖股票的最佳时机 II(贪心)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)-1):
            max_profit += max(0, prices[i+1]-prices[i])
        return max_profit

#455. 分发饼干
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ##典型的贪心算法：先排序，倒序最好。让最大饼干的满足最贪心的小朋友，如果当前的饼干不能满足当前的小朋友，就找下一个小朋友看是否能满足
        gi = 0 ## g:小朋友的胃口，也就是贪心值
        si = 0 ## s:饼干值
        g.sort(reverse=True) ##倒序输出
        s.sort(reverse=True)
        res = 0
        lens_g = len(g)
        lens_s = len(s)
        while gi<lens_g and si<lens_s:
            if s[si]>=g[gi]:
                res+=1
                si+=1
                gi+=1
            else:
                gi+=1 ##看一下小朋友的胃口是否能满足当前的饼干
        return res