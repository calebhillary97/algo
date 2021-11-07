# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")

l = [8, 5, 3, 7, 1, 6, 2, 4]

def mergeSortedArr(a1, a2):
    i=0
    n=len(a1)
    j=0
    m=len(a2)
    new = []
    while(i<n and j<m):
        if(a1[i]<a2[j]):
            new.append(a1[i])
            i+=1
        else:
            new.append(a2[j])
            j+=1
    while(i<n):
        new.append(a1[i])
        i+=1
    while(j<m):
        new.append(a2[j])
        j+=1
    return new
        
# testMerge = mergeSortedArr([1, 3, 5, 7], [2, 4, 6, 8])

# print(testMerge)
# print(testMerge[0:4])
# print(testMerge[4:8])

def mergeSort(arr):
    n = len(arr);
    if(n>2):
        mid = int(n/2)
        print("Mid - "+str(mid))
        left = arr[0:mid]
        right = arr[mid:n]
        
        left = mergeSort(left)
        right = mergeSort(right)
        
        return mergeSortedArr(left, right)
    elif n==2:
        if(arr[0]>arr[1]):
            t = arr[0]
            arr[0] = arr[1]
            arr[1] = t
    return arr
    
print(mergeSort(l))
        
        
        
        
        
        
