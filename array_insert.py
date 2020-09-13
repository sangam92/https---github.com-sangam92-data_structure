a = [1,2,3,4,5]
idx = 2
value=[7]



def insert_gen(a,idx,value):
    b=a[:idx] + value + a[idx:]
    return b


def delete_gen(a,idx):
    b=a.pop(idx)
    return a

def delete_gen2(a,idx):
    b = a[:idx] + a[idx:]
    return b

def update_gen(a,idx,value):
    b = a[:idx]+value + a[idx+1:]
    return b
final = insert_gen(a,idx,value)

print(final)

final_del = delete_gen(a,idx)

print(final_del)

final_del_2 = delete_gen2(a,idx)
print(final_del_2)

upd_gen = update_gen(a,idx,value)
print(upd_gen)
