class Solution:
    def reverseString(self, s: object):
        left = 0
        right = len(s) - 1
        while left <= right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s

t = int(input("Enter the test cases: "))
for _ in range(t):
    s = list(map(str, input("Enter string array: ").strip().split()))
    Obj = Solution()
    ans = Obj.reverseString(s)
    print(ans)

# Time Complexity - O(N)
# Space Complexity - O(1)
