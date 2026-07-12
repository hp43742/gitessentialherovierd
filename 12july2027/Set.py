#set example
set1 = {1, 2, 3, 4, 5}
print(set1)
set2 = {"apple", "banana", "cherry"}
print(set2)
set3 = {1, 2, 3, "hello", True, False}
print(set3) 
set4 = {1, 2, 3, 4, 5, 1, 2, 3}  # Duplicate values will be removed
print(set4)  # Output: {1, 2, 3, 4  
set5 = set([1, 2, 3, 4, 5])  # Creating a set from a list
print(set5)  # Output: {1, 2, 3, 4
set6 = set("hello")  # Creating a set from a string
print(set6)  # Output: {'h', 'e', 'l', 'o'}
set7 = set()  # Creating an empty set
print(set7)  # Output: set()
set8 = {1, 2, 3, 4, 5}
set8.add(6)  # Adding an element to the set
print(set8)  # Output: {1, 2, 3, 4  
set8.remove(3)  # Removing an element from the set
print(set8)  # Output: {1, 2, 4, 5
set8.update({7, 8, 9})  # Adding multiple elements to the set
print(set8)  # Output: {1, 2, 4, 5, 7, 8, 9}
set8.pop()  # Removing a random element from the set
print(set8)  # Output: {2, 4, 5, 7, 8, 9} (random element removed)      
set8.copy()  # Creating a copy of the set

set8.difference(set4)  # Finding the difference between two sets
print("Difference:", set8.difference(set4))  # Output: {6, 7, 8, 9} (elements in set8 but not in set4)

set8.difference_update(set4)  # Updating set8 with the difference from set4
print("After difference update:", set8)  # Output: {6, 7, 8, 9}

set8.intersection(set4)  # Finding the intersection of two sets
print("Intersection:", set8.intersection(set4))  # Output: {1, 2,

set8.intersection_update(set4)  # Updating set8 with the intersection from set4
print("After intersection update:", set8)  # Output: {1, 2, 4, 5

set8.isdisjoint(set4)  # Checking if two sets are disjoint
print("Is disjoint:", set8.isdisjoint(set4))  # Output: False (sets have common elements

set8.issubset(set4)  # Checking if set8 is a subset of set4
print("Is subset:", set8.issubset(set4))  # Output: True (set8 is a subset of set4)

set8.issuperset(set4)  # Checking if set8 is a superset of set4
print("Is superset:",set8.issuperset(set4))  # Output: False (set8 is not a superset of set4)  

set8.symmetric_difference(set4)  # Finding the symmetric difference between two sets
print("Symmetric difference:", set8.symmetric_difference(set4))  # Output: {6, 7, 8, 9} (elements in either set8 or set4 but not in both)

set8.symmetric_difference_update(set4)  # Updating set8 with the symmetric difference from set4
print("After symmetric difference update:", set8)  # Output: {6, 7, 8, 9}

set8.union(set4)  # Finding the union of two sets
print("Union:", set8.union(set4))  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9} (all unique elements from both sets)

set8.update(set4)  # Updating set8 with the union from set4
print("After update:", set8)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

set8.clear()  # Clearing all elements from the set
print("After clear:", set8)  # Output: set() (empty set)    
