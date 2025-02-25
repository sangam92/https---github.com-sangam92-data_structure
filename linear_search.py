elem = [2,33,12,45,12]
val = 1
match =0
def linear_search(elem,val):
    match =0

    for i in elem:
        if i ==val:
            print(i,"element found")
    return -1


linear_search(elem,val)
