class Stack:
    def __init__(self):
        self.arr = []

    def push(self, data):
        self.arr.append(data)
        return self.arr

    def pop(self):
        if len(self.arr) == 0:
            return -1
        else:
            return self.arr.pop()


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
        print()
