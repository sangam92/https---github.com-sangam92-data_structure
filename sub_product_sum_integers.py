"""
1281. Subtract the Product and Sum of Digits of an Integer

"""


def sum_product(nums):
    sum=0
    product = 1
    final_op=0
    for i in nums:
        sum = sum + i
        product = product  * i
    final_op=sum + product
    return final_op

if __name__ == '__main__':
    nums = 234
    op = sum_product(nums)
    print(op)
