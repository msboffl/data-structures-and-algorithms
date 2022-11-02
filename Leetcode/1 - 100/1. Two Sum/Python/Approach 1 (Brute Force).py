class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(0, n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]


t = int(input("Enter the test cases: "))
for _ in range(t):
    nums = list(map(int, input("Enter the nums array: ").split()))
    target = int(input("Enter target value: "))
    Obj = Solution()
    ans = Obj.twoSum(nums, target)
    print(ans)

# Time Complexity = O(N*N = N^2)
# Space Complexity = O(N)
