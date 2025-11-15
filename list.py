# List creation
numbers = [10, 20, 30, 40, 50]
mixed = [1, "Dhruv", True, 4.5]

print(numbers[0])      # 10
print(numbers[-1])     # 50
print(numbers[1:4])    # [20, 30, 40]


#list method 

fruits = ["apple", "banana", "cherry"]

fruits.append('orange')#last insert the data
fruits.insert(1,"new") # add at specific index
print(fruits)

fruits.remove("banana")     # remove specific item
popped = fruits.pop()       # removes last item
print("Popped item:", popped)

print("After pop:", fruits)

fruits.sort()               # sort ascending
print("Sorted list:", fruits)

fruits.reverse()            # reverse order
print("Reversed list:", fruits)

squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)