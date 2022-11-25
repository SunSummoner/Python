#Library Sort

array = []
ar2=[]
#intialising the array

def binary_search(arr, low, high, x,gap):
 
    # Check base case
    if high >= low:
 
        mid=(high +low)//2
        
        if arr[mid]==x:
            arr[mid+1]=x
        elif arr[mid]<x && arr[mid+gap]>x :
            arr[mid +1]=x
        elif:
            arr[mid-gap +1]=x
 

n= int(input("Enter the number of elements in the array:"))

print("Enter the elements:")

ch= input("Do you want to decide the gap?(Y/N)")

if (ch=='y' or ch=='Y'):
    gap=int(input("Input the gap:"))

else:
    gap=n/4

array2=[]

for i in range(0,n):
    x=int(input("Element", i, ':'))
    array[i]=x
    while (i*gap) < n:
        arr2[i*gap]=x
    else:
        binary_search(arr2, 0, n*4, x, gap)

arr3=[]
for h in range (0,n*4):
    for k in range (0,n):
        if arr2[h]==array[k]:
            arr3[k]=arr2[h]
    
