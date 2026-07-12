# Tuple operations example

# Creating tuples
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

# Accessing tuple elements
print(my_tuple[0])

# Tuple unpacking
a, b, c, d, e = my_tuple
print(a, b, c)  # Example

list1=list(my_tuple)
print(list1)  # Convert tuple to list
print(type(list))  # Output: <class 'list'>


#tuple with loop
for i in my_tuple:  
    
    print(i)  # Output: 1 2 3 4 5


    for i in range(0, len(my_tuple),2):
        print(my_tuple[i])  # Output: 1 2 3 4 5




