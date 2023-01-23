import array

arr=array.array('i',[4,5,8,9,3])

# printing created array
print("Printing array: ", end=" ")
for i in range (0,5):
    print(arr[i], end=" ")

print("\r") #This is for next line

# adding new element on exiating array

arr.append(9)
print("After adding new element: ", end=" ")
for i in range (0,6):
    print(arr[i],end=" ")
print("\r")

#insearting ilement in the desire index
arr.insert(2,6)
print("After insearting the element on the desire index: ",end=" ")
for i in range(0,7):
    print(arr[i],end=" ")
print("\r")
#remove element by their value
 
arr.remove(9)
print("After removeing  element 5: ",end=" ")
for i in range (0,6):
    print(arr[i],end=" ")
print("\r")

#remove element by their index

arr.pop(3)
print("After poping element by their index: ",end=" ")
for i in range (0,5):
    print(arr[i],end=" ")
print("\r")
#finding index of avilable element form an array

print("Index of element 6 is : " ,end=" ")
print(arr.index(6))
print("\r")

#reversing whole array

arr.reverse()
print("After reversing array: ",end=" ")
for i in range(0,5):
    print(arr[i],end=" ")
print("\r")

