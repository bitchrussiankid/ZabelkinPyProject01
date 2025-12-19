# create a list:
numbers = [5, 1, 9, 3, 7]
print(numbers)

# sort the list:
numbers.sort()
print(numbers)

# replacing a list element:
numbers[2] = 100
print(numbers)

# copy a slice of the list:
sliceNumbers = numbers[1:]
print(sliceNumbers)

# remove the last element of the original list:
del numbers[-1]
print(numbers)