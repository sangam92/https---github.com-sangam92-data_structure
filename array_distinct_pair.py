## find the distinct pair with difference k

a = [1,4,6,7,8,10,14,3]

k = 3

a = sorted(a)

count = 0

for j in range(len(a)-1):

    for i in range(len(a)-1):
        if a[j] - a[i] == k:
            count = count + 1


print(count)

print(a)
