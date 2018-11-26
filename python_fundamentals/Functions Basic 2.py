#1 
def a(num):
    arr=[]
    for i in range(num,-1,-1):
        arr.append(i)
    return arr
print(a(5))


#2 
def a(arr):
    print arr[0]
    return arr[1]

#3
def a(arr):
    sum=arr[0]+len(arr)
    return sum
print(a([1,2,3]))

#4 
def a(arr):
    arr2=[]
    for i in range (0, len(arr)):
        if(arr[i]>arr[1]):
            arr2.append(arr[i])
    print len(arr2)
    return arr2
print(a([2,1,3,4,5]))

#5 
def a(size,value):
    arr2=[]
    for i in range (0,size):
        arr2.append(value)
    return arr2
print(a(3,1))
