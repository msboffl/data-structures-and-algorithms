class Solution:
    def removeElement(self, nums, val):
        n = len(nums)
        length = 0
        for i in range(0, n):
            if nums[i] != val:
                nums[length] = nums[i]
                length += 1
        return length




t = int(input("Enter test cases: "))
for _ in range(t):
    nums = list(map(int, input('Enter nums: ').split()))
    val = int(input("Enter remove element: "))
    Obj = Solution()
    ans = Obj.removeElement(nums, val)
    print(ans)