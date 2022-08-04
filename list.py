list1 = [5, 4, 17, 19, 30, 2, 7, 10, 45]

# sum all the items in the list.
sumOfTheList = sum(list1)
print(sumOfTheList)

# printing the largest element
print("Largest element is:", max(list1))
# or we could use sort fun to sort the list
list1.sort()
print("Largest element is:", list1[-1])

# using List Comprehension , create a new list from the above list containing only even numbers.

ComprehensionList = [i for i in list1 if i % 2 == 0]
print(ComprehensionList)

newList = list1[0:6]
print(newList)