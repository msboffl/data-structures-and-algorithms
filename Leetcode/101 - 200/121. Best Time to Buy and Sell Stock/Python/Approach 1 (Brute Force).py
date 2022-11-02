class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        max_profit = 0
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                profit = prices[j] - prices[i]

                if profit > max_profit:
                    max_profit = profit

        return max_profit


t = int(input("Enter the test cases: "))
for _ in range(t):
    prices = list(map(int, input("Enter the prices: ").split()))
    Obj = Solution()
    ans = Obj.maxProfit(prices)
    print(ans)

# Time Complexity - O(N*N = N^2)
# Space Complexity = O(1)
