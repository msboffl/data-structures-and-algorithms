class Solution:
    def removeElement(self, nums, val):
        n = len(nums)
        length = 0
        for i in range(0, n-length):
            if nums[i] == val:
                for j in range(i, n-length-1):
                    nums[j] = nums[j+1]
                length += 1
                i -= 1

        return n - length - 1


t = int(input("Enter test cases: "))
for _ in range(t):
    nums = list(map(int, input('Enter nums: ').split()))
    val = int(input("Enter remove element: "))
    Obj = Solution()
    ans = Obj.removeElement(nums, val)
    print(ans)