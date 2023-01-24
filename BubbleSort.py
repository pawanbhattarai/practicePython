def BubbleSort(arr):
    n=len(arr)
    swaped=False

    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                swaped=True
                arr[j],arr[j+1]=arr[j+1],arr[j]

    if not swaped:
          return

arr=[3,4,2,0,7,5,9,1]
BubbleSort(arr)
print("Sorted Array is: ", end=" ")
for i in range (len(arr)):
    print(arr[i],end=" ")