class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        mini = prices[0]
        max_profit = 0
        for i in range(1, n):
            profit = prices[i] - mini
            max_profit = max(max_profit, profit)
            mini = min(mini, prices[i])
        return max_profit


t = int(input("Enter the test cases: "))
for _ in range(t):
    prices = list(map(int, input("Enter the prices: ").split()))
    Obj = Solution()
    ans = Obj.maxProfit(prices)
    print(ans)

# Time Complexity - O(N)
# Space Complexity = O(1)
