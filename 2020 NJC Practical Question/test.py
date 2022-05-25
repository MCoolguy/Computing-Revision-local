def bubblesort(lst):
    n = len(lst)
    for i in range(1,n):
        for j in range(n-1):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
                
    return lst

list = [1,5,3,4,2,7]
#print(bubblesort(list))

def insert(lst):
    n = len(lst)
    for i in range(1,n):
        j = i 
        while j>=0 and lst[j]<lst[j-1]:
            lst[j],lst[j-1] = lst[j-1],lst[j]
            j-=1
            
    return lst

#print(insert(list))

def mergesort(lst):
    n = len(lst)
    if n==1:
        return lst
    
    left = lst[:n//2]
    right = lst[n//2:]
    
    left = mergesort(left)
    right = mergesort(right)
    
    return merge(left,right)

def merge(left,right):
    finalst = []
    while len(left)!=0 and len(right)!=0:
        if left[0]>right[0]:
            finalst.append(right[0])
            right.pop(0)
        else:
            finalst.append(left[0])
            left.pop(0)
            
    while len(left)!=0:
            finalst.append(left[0])
            left.pop(0)
            
    while len(right)!=0:
        finalst.append(right[0])
        right.pop(0)
        
        
    return finalst
print(mergesort(list))
        
        