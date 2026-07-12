#dictionary examples

#ordered, indexed, mutable,hetrogenious data type

dict1 = {"name": "John", 
         "age": 30, 
         "city": "New York",
         "dept": "IT"} 
print(dict1)
print("name:", dict1["name"])  # Accessing a specific value
print("Age:", dict1["age"])   # Accessing another specific value
print("City:", dict1["city"])  # Accessing the third specific value
print("Department:", dict1["dept"])  # Accessing the fourth specific value 

dict1["name"] = "Himanshu"  # Modifying an existing value
print("Updated name:", dict1["name"])  # Accessing the updated value
dict1["country"] = "USA"  # Adding a new key-value pair
print("Country:", dict1["country"])  # Accessing the newly added value      

dict2 = dict(name="Alice", age=25, city="Los Angeles")  # Creating a dictionary using the dict() constructor
print(dict2)  # Printing the second dictionary  

dict1.pop("age")  # Removing a key-value pair using pop()
print("After removing age:", dict1)  # Printing the dictionary after removal        

del dict1["city"]  # Removing a key-value pair using del
print("After deleting city:", dict1)  # Printing the dictionary after deletion  

popvalue = dict1.pop("dept")  # Removing a key-value pair and storing the removed value
print("Removed department:", popvalue)  # Printing the removed value

# print(dict1.get())  # Accessing the value using the get() method
print(dict1.items())  # Printing all key-value pairs as a view object
print(dict1.keys())  # Printing all keys as a view object
print(dict1.values())  # Printing all values as a view object


dict1 = {"name": "John", 
         "age": 30, 
         "city": "New York",
         "dept": "IT"} 

print("Iterating through the dictionary keys:")
for i in dict1.keys():  # Iterating through the dictionary keys
    print(i)    

print("Iterating through the dictionary values:")
for i in dict1.values():  # Iterating through the dictionary values 
        print(i)


#index  with loop
for i in range(len(dict1)):
    print(dict1[list(dict1.keys())[i]])  # Accessing values using index and printing them