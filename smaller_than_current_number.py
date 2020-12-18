"""
1365. How Many Numbers Are Smaller Than the Current Number

"""

def smallerthancurrent(nums):
    final_op =[]
    for i in nums:
        count=0
        for j in nums:

            if i > j:
                count = count + 1
        final_op.append(count)
    return final_op

if __name__ == '__main__':
    nums = [8,1,2,2,3]
    sc=smallerthancurrent(nums)
    print(sc)
