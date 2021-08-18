"""
Heap and operation

"""
import heapq

arr=[1,1,1,2,2,3,-2,-3]

k=3

heapq.heapify(arr)

print(heapq.nlargest(k,arr))

print(heapq.nsmallest(k,arr))