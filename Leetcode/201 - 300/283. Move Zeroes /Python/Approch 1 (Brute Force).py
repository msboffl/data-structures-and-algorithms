class Solution:
    def moveZeros(self, nums):
        n = len(nums)
        for i in range(0, n):
            for j in range(i+1, n):
                if nums[i] == 0 and nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums


t = int(input("Enter the test cases: "))
for _ in range(t):
    nums = list(map(int, input("Enter nums: ").split()))
    Obj = Solution()
    ans = Obj.moveZeros(nums)
    print(ans)

# Time Complexity  - O(N*N = N^2)
# Space Complexity - O(1)
