class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        i = 0
        j = i + 1

        # 7, 3, 4, 5, 6, 2, 8, 1

        while(j < len(prices)):
            if prices[i] >= prices[j]:
                i = j
                j += 1

            elif prices[i] < prices[j]:
                res = max(res, prices[j] - prices[i])
                j += 1

        return res