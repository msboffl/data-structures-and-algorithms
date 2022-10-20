class Stack:
    def __init__(self):
        self.arr = [0] * 10
        self.top = -1

    def push(self, data):
        self.top += 1
        self.arr[self.top] = data

    def isEmpty(self):
        return self.top == -1

    def isSize(self):
        return self.top + 1

    def pop(self):
        if len(self.arr) == 0:
            return -1

        popElement = self.arr[self.top]
        self.arr[self.top] = 0
        self.top -= 1
        return popElement


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        s = Stack()
        n = int(input())
        ls = list(map(int, input().split()))
        i = 0
        while i < len(ls):
            if ls[i] == 1:
                s.push(ls[i + 1])
            elif ls[i] == 2:
                print(s.pop(), end=" ")
                i = i + 1
            elif s.isEmpty():
                print(-1)
                i = i + 1
        print(s.isSize())
