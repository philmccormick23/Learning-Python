#1 
def a(arr):
    for i in range (0,len(arr)):
        if(arr[i]>0):
            arr[i]="big"
    return arr
        
print(a([1,2,3,4]))

#2
def a(arr):
    numPos=0
    for i in range (0,len(arr)):
        if(arr[i]>0):
            numPos+=1
    arr.append(numPos)
    return arr
        
print(a([1,2,3,4]))

#3 
def a(arr):
    sum=0
    for i in range (0,len(arr)):
        sum+=arr[i]
    return sum
        
print(a([1,2,3,4]))

#4 **why won't it give decimal outputs if the array has integers? 
def a(arr):
    sum=0
    for i in range (0,len(arr)):
        sum+=arr[i]
    avg=sum/(len(arr))
    print(avg)
        
print(a([1,2,3,4.0]))

#5 
def a(arr):
    return len(arr)
        
print(a([1.0,2,3,4]))

#6 
def a(arr):
    min=arr[0]
    for i in range (0,len(arr)):
        if(arr[i]<min):
            min=arr[i]
    return min
print(a([1,2,3,4]))

#7 
def a(arr):
    max=arr[0]
    for i in range (0,len(arr)):
        if(arr[i]>max):
            max=arr[i]
    return max
print(a([1,2,3,4]))

#8
def a(arr):
    ultraAnalyze={'sum':0, 'avg':0, 'min':arr[0],'max':arr[0],'length':len(arr)}  
    for i in range (0,len(arr)):
        ultraAnalyze['sum']+=arr[i]
        if(arr[i]<ultraAnalyze['min']):
            ultraAnalyze['min']=arr[i]
        if(arr[i]>ultraAnalyze['max']):
            ultraAnalyze['max']=arr[i]
    ultraAnalyze['avg']=ultraAnalyze['sum']/len(arr)
    return ultraAnalyze
   
print(a([1,2,3,4]))

#9
def a(arr):
    arr2=[]
    for i in range (len(arr)-1,-1,-1):
        arr2.append([arr[i]])
    return arr2
        
print(a([1,2,3,4]))
