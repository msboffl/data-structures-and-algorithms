class Solution:
    def deleteAtAny(self, arr):
        length: int = 0
        for i in range(0, len(arr)):
            arr[length] = arr[i]
            length += 1

        # print(length)
        # Delete at Index 2
        for i in range(3, length):
            arr[i-1] = arr[i]
            # newArray.append(arr[i])
        length -= 1

        newArray = [0] * length
        for i in range(0, length):
            newArray[i] = arr[i]
        return newArray


t = int(input('Enter the test cases: '))
for _ in range(t):
    n = int(input("Enter no. of elements: "))
    arr = list(map(int, input('Enter the arr: ').split(' ')))
    Obj = Solution()
    ans = Obj.deleteAtAny(arr)
    print(ans)