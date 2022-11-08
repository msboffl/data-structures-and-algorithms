arr = [0] * 10                  # Create a new array with a capacity of 10.
length = 0                      # Current length is 0, because it has 0 elements.
for i in range(0, 6):    # Add 3 items into it
    arr[i] = i * i
    length += 1                 # Each time we add an element, the length goes up by one.

print("Array Length is: ", length)
print("Array Capacity is: ", len(arr))


