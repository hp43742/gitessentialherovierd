#this is example of list array 

list1 = [1,2,3,4,5]
print(list1)
list2 = ["himanshu","hello","world"]
print(list2)
list3 = [1,2,3,"hello",True,False]
print(list3)

print(list1[0])
print(list2[1])
print(list3[3]) 
print(list1[0:3]) #slicing of list  
#pritn list values using for loop
for i in list1:
    print(i)        

#printlist values using while loop
i = 0
while i < len(list2):

    print(list2[i])
    i += 1

#print list values using for loop with index
for i in range(len(list3)):
    print(list3[i])


    #print list values using for loop with index and enumerate function
for index, value in enumerate(list3):
    print(index, value)


    #printlistvale's position 
    position = list3.index("hello")
print("position",position)  # Output: 3


#list slicing

print(list1[3:6])  # Output: [2, 3, 4]


#list functions

list1.append(6)
print("append value 6:", list1)  # Output: [1, 2, 3, 4, 5, 6]
list1.insert(2, 2.5)
print("insert at value 2.5:", list1)  # Output: [1, 2, 2.5, 3, 4, 5, 6]
list1.remove(2.5)
print(list1)  # Output: [1, 2, 3, 4, 5, 6]
list1.pop()
print("pop function remove last value:",list1)  # Output: [1, 2, 3, 4, 5]
list1.sort()
print(list1)  # Output: [1, 2, 3, 4, 5]     
list1.reverse()
print("reverse function:", list1)  # Output: [5, 4, 3, 2, 1]
list1.extend([6, 7, 8])
print("extend function add value 6 ,7 ,8 :", list1)  # Output: [5, 4, 3, 2, 1,  6, 7, 8]   
list1.count(3)
print("count function:", list1.count(3))  # Output: 1

list11=["a","b","c"]
for i in range(0, len(list11)):
    print("list11 values:", i, list11[i])  # Output: a b c 
