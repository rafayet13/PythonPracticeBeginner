#slicing list
some_marks = [2, 4, 6, 32, 60, 65, 69, 76, 80, 85, 90]
avg_marks = some_marks[4:8]
print(avg_marks)
good_marks = some_marks[8:]
print(good_marks)
poor_marks = some_marks[:4]
print(poor_marks)



print("\n")
#jump in list where: [: : ] first 2 is start & end poin and last is jump value
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[2:9:3])


print("\n")
#slicing in reverse mode
squares = [1, 2, 5, 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 4, 6, 7, 8]
print(squares[3:-4])


print("\n")
#revese list -1 is index value from reverse position
values = [3, 4, 5, 6, 7, 8]
print(values[::-1])


print("\n")
# Prints the minimum value among all the elements of the list below
print("min",min([1, 2, 3, 4, 0, 2, 1]))
# Prints the maximum value among all the elements of the following list
print("max",max([1, 4, 9, 2, 5, 6, 8]))
# Print sum of all the elements of the following list
print("sum",sum([1, 2, 3, 4, 5]))
