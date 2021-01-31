"""
No with max occurences
"""

def max_occurence(arr):
    if len(arr) ==0:
        return 0
    else:

        dic ={}
        for i in arr:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        print(max(dic,key=dic.get))

arr=[]

print(max_occurence(arr))