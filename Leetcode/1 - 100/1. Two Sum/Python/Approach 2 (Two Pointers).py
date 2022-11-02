class Solution:
    def twoSum(self, nums, target):
        arr = []
        for i, x in enumerate(nums):
            arr.append([x, i])
        arr.sort()

        left = 0
        right = len(arr)-1
        while left < right:
            sum1 = arr[left][0] + arr[right][0]
            if sum1 == target:
                return [arr[left][1], arr[right][1]]
            elif sum1 > target:
                right -= 1
            else: left += 1


t = int(input("Enter the test cases: "))
for _ in range(t):
    nums = list(map(int, input("Enter the nums array: ").split()))
    target = int(input("Enter target value: "))
    Obj = Solution()
    ans = Obj.twoSum(nums, target)
    # print(ans)

# Time Complexity = O(N*LogN)
# Space Complexity = O(N)
