"""

Number of Good Pairs

"""


def good_pairs(nums):
    count=0
    for i in range(0,len(nums)):
        for j in range(1,len(nums)):
            #+print(nums[i],nums[j],i,j)
            if nums[i]==nums[j] & i < j:
                print(nums[i],nums[j],i,j)
                count = count +  1
    return count


if __name__ == '__main__':
    nums = [1,2,3,1,1,3]
    gp = good_pairs(nums)
    print(gp)
