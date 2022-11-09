class Solution:
    def searchIndex(self, arr, target):
        for i in range(0, len(arr)):
            if arr[i] == target:
                return i


t = int(input('Enter the test cases: '))
for _ in range(t):
    n = int(input("Enter no. of elements: "))
    arr = list(map(int, input('Enter the arr: ').split(' ')))
    target = int(input('Enter search value: '))
    Obj = Solution()
    ans = Obj.searchIndex(arr, target)
    print(ans)