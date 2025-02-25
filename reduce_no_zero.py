"""
1342. Number of Steps to Reduce a Number to Zero

"""

def numberofsteps(num):
    count=0
    while (num!=0):

        if num % 2==0:
            num=num/2
        else:
            num = num - 1
        count = count + 1
    return count

if __name__ == '__main__':
    num = 123
    no_steps=numberofsteps(num)
    print(no_steps)
