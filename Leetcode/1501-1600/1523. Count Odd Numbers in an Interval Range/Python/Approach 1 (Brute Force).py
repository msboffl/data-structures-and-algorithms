class Solution:
    def countOdds(self, low, high):
        count = 0
        for i in range(low, high + 1):
            if i % 2 == 1:
                count += 1
        return count


t = int(input("enter t cases: "))
for _ in range(t):
    low, high = map(int, input("Enter low, high values: ").strip().split())
    Obj = Solution()
    ans = Obj.countOdds(low, high)
    print(ans)

# Time Complexity  - O(N)
# Space Complexity - O(1)
