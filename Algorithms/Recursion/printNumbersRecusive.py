# Print the Numbers 0 to N (Reverse)

class Solution:
    def printNumbers(self, n):
        if n == 0:
            return 0
        print(n)
        return self.printNumbers(n - 1)


t = int(input("Enter the test cases: "))
for _ in range(t):
    n = int(input("Enter the number: "))
    Obj = Solution()
    ans = Obj.printNumbers(n)
    print(ans)

# Time Complexity - O(N)
# Space Complexity - O(N)
