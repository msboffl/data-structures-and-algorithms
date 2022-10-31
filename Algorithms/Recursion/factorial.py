class Solution:
    def factorialFind(self, num):
        if num == 0 or num == 1:
            return 1
        else:
            return num * self.factorialFind(num - 1)


t = int(input("Enter the test cases: "))
for _ in range(t):
    num = int(input("Enter the number: "))
    Obj = Solution()
    ans = Obj.factorialFind(num)
    print(ans)
