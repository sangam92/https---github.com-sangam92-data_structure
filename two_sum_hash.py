"""
Two Sum Problem using Hash

"""


def twosumhash(nums, key):
    sum = []
    hashtables = {}

    for i in range(len(nums)):
        comp = key - nums[i]
        if comp in hashtables:
            print(nums.index(comp),i)
        hashtables[nums[i]] = nums[i]

nums=[4,5,1,8]
key = 9

twosumhash(nums,key)
