def rotate(arr,k):
 
    new_arr=[]
    new_arr=arr[k+1:]+arr[0:k+1]
    return new_arr

if __name__ == '__main__':
    arr=[1,2,0,4,5,6,7,8,9]
    d=3

    print("Original array is: ",end=" ")
    for i in arr:
        print(i,end=" ")
    print("\r")
   
    arr=rotate(arr,d)
    print("After rotating by 3rd position: ",end=" ")
    for i in arr:
       print(i,end=" ")