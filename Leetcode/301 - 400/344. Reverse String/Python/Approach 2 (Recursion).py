class Solution:
    def reverseRecursion(self, left, right, s):
        if left >= right:
            return s
        s[left], s[right] = s[right], s[left]
        return self.reverseRecursion(left + 1, right - 1, s)

    def reverseString(self, s: object):
        self.reverseRecursion(0, len(s) - 1, s)
        return s


t = int(input("Enter the test cases: "))
for _ in range(t):
    s = list(map(str, input("Enter string array: ").strip().split()))
    Obj = Solution()
    ans = Obj.reverseString(s)
    print(ans)

# Time Complexity - O(N)
# Space Complexity - O(N)
