class Solution:
    def moveZeros(self, nums):
        n = len(nums)
        zero = 0
        for i in range(0, n):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
        return nums


t = int(input("Enter the test cases: "))
for _ in range(t):
    nums = list(map(int, input("Enter nums: ").split()))
    Obj = Solution()
    ans = Obj.moveZeros(nums)
    print(ans)

# Time Complexity  - O(N)
# Space Complexity - O(1)