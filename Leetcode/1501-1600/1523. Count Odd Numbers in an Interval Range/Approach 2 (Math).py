class Solution:
    def countOdds(self, low, high):
        if low % 2 == 1 and high % 2 == 1:
            return (high - low) // 2 + 1
        return (high - low + 1) // 2


t = int(input("enter t cases: "))
for _ in range(t):
    low, high = map(int, input("Enter low, high values: ").strip().split())
    Obj = Solution()
    ans = Obj.countOdds(low, high)
    print(ans)

# Time Complexity  - O(1)
# Space Complexity - O(1)
