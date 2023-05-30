#!/usr/bin/python

#mergesort algorithm

def mergesort(data):
    #divido el array en dos
    if len(data)>1:
        mid = len(data)//2
        left = data[:mid]
        right = data[mid:]

        mergesort(left)
        mergesort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                data[k] = left[i]
                i+=1
                k+=1
            else:
                data[k] = right[j]
                j+=1
                k+=1

        # if left still has items                
        while i<len(left):
            data[k] = left[i]
            k+=1
            i+=1
        #if right still has values
        while j<len(right):
            data[k] = right[j]
            j+=1
            k+=1
        
    



    

myList=[9,2,4,8,24,98,26,44,23]

print(myList)
mergesort(myList)
print(myList)