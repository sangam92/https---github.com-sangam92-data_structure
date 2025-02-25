# Adding two numbers to return the target value , output will be index of those numbers

## a = [1,2,3,4,5]

##target = 9

##output =[3,4]

def array_two(a,target):
    output = []
    for j in range(len(a)):
        for i in range(len(a)):
            print(a[i],a[j])
            if a[j] + a[i] == target:
                output.append(i)
                output.append(j)
    return output


a=[1,2,3,4,5]
target=9

two = array_two(a,target)
print(two)
