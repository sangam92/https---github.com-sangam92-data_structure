"""

Kids with extra candies

"""

def extracandies(can, ecan):
    max_can = max(can)
    print(max_can)
    output = []
    for i in can:
        i = i + ecan
        if i >= max_can:
            output.append(True)
        else:
            output.append(False)
    return output
    
if __name__ == '__main__':
    can = [2,3,5,1,3]
    ecan = 3
    final =extracandies(can,ecan)
    print(final)
