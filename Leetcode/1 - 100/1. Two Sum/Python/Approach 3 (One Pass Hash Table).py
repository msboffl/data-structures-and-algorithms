class Solution:
    def twoSum(self, nums, target):
        hashMap = {}
        for i in range(len(nums)):
            otherNumber = target - nums[i]

            if otherNumber in hashMap:
                return [hashMap[otherNumber], i]
            hashMap[nums[i]] = i


t = int(input("Enter the test cases: "))
for _ in range(t):
    nums = list(map(int, input("Enter the nums array: ").split()))
    target = int(input("Enter target value: "))
    Obj = Solution()
    ans = Obj.twoSum(nums, target)
    print(ans)

# Time Complexity = O(N)
# Space Complexity = O(N)
