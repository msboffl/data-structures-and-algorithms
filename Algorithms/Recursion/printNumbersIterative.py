# Print the Numbers 0 to N (Reverse)
class Solution:
    def printNumbers(self, n):
        for i in range(n, -1, -1):
            print(i)


t = int(input("Enter the test cases: "))
for _ in range(t):
    n = int(input("Enter the number: "))
    Obj = Solution()
    Obj.printNumbers(n)
    # print(ans)

# Time Complexity - O(N)
# Space Complexity - O(1)
