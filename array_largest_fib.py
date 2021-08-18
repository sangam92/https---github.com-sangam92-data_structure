# array to find the largest subset of a fibonnaci number

def fibonnaci(b):

    if b == 0:
        return 1
    else:
        return b*fibonnaci(b-1)

a = [2,3,1,4,5,6,7,10,3]

b= max(a)
print(b)

c= fibonnaci(b)

print(c)
