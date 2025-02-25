#From the given array, find a subarray that has at least k numbers and has the largest possible sum.

a = [2,43,52,5,12,3,90,6]

a =sorted(a)
sum_a=0
sum_b = 0
ele = 0
for i,j in zip(range(len(a)-1),range(len(a)-1,1)):
    print(i,j)
    sum_a = a[i] + sum_a
    print(sum_a)
    ele.append(j)
    sum_b = a[j] + sum_b
    print(sum_b)
    if sum_b > sum_a:
        break
print(ele)
