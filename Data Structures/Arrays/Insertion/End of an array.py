arr = [0] * 10
length = 0
for i in range(0, 5):
    arr[length] = i
    length += 1
print("Array Length is: ", length)


# Insertion at End
arr[length] = 15
length += 1

print("Array of Insertion: ", arr)
print('Array Length after insertion: ', length)


