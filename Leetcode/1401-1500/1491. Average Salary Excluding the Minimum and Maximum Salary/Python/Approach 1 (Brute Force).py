class Solution:
    def avarage(self, salary):
        n = len(salary)

        Max = Min = salary[0]
        for i in range(1, n):

            if salary[i] <= Max:
                Max = salary[i]
            if salary[i] > Min:
                Min = salary[i]
        # print(Max, Min)

        avg = 0
        for i in range(0, n):
            if salary[i] != Max and salary[i] != Min:
                avg += salary[i]

        return avg / (n - 2)


t = int(input("enter t cases:"))
for _ in range(t):
    salary = list(map(int, input("Enter salary: ").strip().split()))
    Obj = Solution()
    ans = Obj.avarage(salary)
    print(ans)