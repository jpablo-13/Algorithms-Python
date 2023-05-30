#!/usr/bin/python

def quicksort(data,first,last):
    if first<last:
        #calculate the pivot point
        piv = partition(data,first,last)
   
        #sort the partitions
        quicksort(data,first,piv-1)
        quicksort(data,piv+1,last)

def partition(part,first,last):
    
    #we start the with pivot at the beginning
    pv = part[first]
    
    #our lower index will be the next to the pivot
    lower = first + 1
    upper = last

    found = False
    #while the pivot position is not found
    while not found:
        
        while (lower <= upper and part[lower] <= pv):
            lower+=1
        while (upper >= lower and part[upper] >= pv):
            upper-=1
       
        if upper<lower:
            found=True
        else:
            t = part[lower]
            part[lower] = part[upper]
            part[upper] = t

    temp = part[first]
    part[first] = part[upper]
    part[upper] = temp
    
    return upper

test = [10, 23, 48, 1, 94, 73, 24, 15, 82, 9, 58, 94]

print(test)
quicksort(test,0,len(test)-1)
print(test)    
