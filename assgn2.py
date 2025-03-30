# Step 1: Create an empty list
myList = []

# Step 2: Append elements to the list
myList.append(10)
myList.append(20)
myList.append(30)
myList.append(40)
print(myList)

# Step 3: Insert the value 15 at the second position in the list
myList.insert(1, 15)
print(myList)

# Step 4: Extend the list with another list [50, 60, 70]
myList.extend([50, 60, 70])
print(myList)

# Step 5: Remove the last element from the list
myList.pop()
print(myList)

# Step 6: Sort the list in ascending order
myList.sort()
print(myList)

# Step 7: Find and print the index of the value 30
indexOf30 = myList.index(30)
print("Index of 30:", indexOf30)
