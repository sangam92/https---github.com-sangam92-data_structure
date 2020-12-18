## Sliding Window Concept
## The maximum of the k subset in the array.

def sliding_window(a,k,n):
    max_val =[]
    val =[]
    val1=[]

    for i in range(n-k-1):
        if i==0:
            val = a[0:k+1]
            print("The value in val variable",val)
            val1 = max(val)
            max_val.append(val1)
        else:
            val = a[i:i*k+1]
            val1 =max(val)
            max_val.append(val1)
    return max_val




##driver Code

a = [15,2,3,4,5,6,2,4,9,1,5]
n =len(a)
k =3
sl=sliding_window(a,k,n)

print(sl)
