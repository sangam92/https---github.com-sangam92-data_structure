#program to rotate array by n index

print("Enter the index rotation value")
n = 2
array_no = [1,2,3,4,5]

ar_len = len(array_no)
print(ar_len)
last = array_no[-1]
for i in range(ar_len-1):

    array_no[i+1] = array_no[i]
array_no[0] = last

print(array_no)
