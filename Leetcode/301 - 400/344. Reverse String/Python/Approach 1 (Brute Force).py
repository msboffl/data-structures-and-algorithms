class Solution:
    def reverseString(self, s):
        n = len(s)
        res = []
        for i in range(n - 1, -1, -1):
            res.append(s[i])
        return res


t = int(input("Enter the test cases: "))
for _ in range(t):
    s = list(map(str, input("Enter string array: ").strip().split()))
    Obj = Solution()
    ans = Obj.reverseString(s)
    print(ans)

# Time Complexity - O(N)
# Space Complexity - O(N)
