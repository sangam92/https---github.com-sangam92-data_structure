"""
Quick Sort Algorithm

"""
def partition(a,low,high):
    i = low+ 1
    j = high
    pivot = a[low]
    while True:
        while ( i<=j and a[i]<= pivot):
            i =i+1
        while ( i<=j and a[j] >= pivot):
            j = j-1
        if i > j:
            break
        else:
            a[i],a[j]=a[j],a[i]
    a[low],a[j]=a[j],a[low]
    return j
def quickSort(arr, low, high): 
	if len(arr) == 1: 
		return arr 
	if low < high: 

		# pi is partitioning index, arr[p] is now 
		# at right place 
		pi = partition(arr, low, high) 

		# Separately sort elements before 
		# partition and after partition 
		quickSort(arr, low, pi-1) 
		quickSort(arr, pi+1, high) 


# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr, 0, n-1) 
print("Sorted array is:") 
for i in range(n): 
	print("%d" % arr[i])

