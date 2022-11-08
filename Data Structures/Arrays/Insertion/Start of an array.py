arr = [0] * 10
length = 0
for i in range(0, 5):
    arr[length] = i
    length += 1
print('Array elements are: ', arr)

# Insertion at Start
for i in range(5, -1, -1):
    arr[i+1] = arr[i]

arr[0] = 10
print('After Insertion: ', arr)