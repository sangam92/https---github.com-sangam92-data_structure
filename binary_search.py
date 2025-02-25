
def binary_search(elem,val,low,high,mid):
    while(low <=high):
      mid = low + high // 2

      if mid == val:
        return val

      elif mid < val :
        low = mid + 1

      else:
        high = mid -1

    return -1
if __name__=="__main__":
    elem = [22,1,45,78,25]
    low =0
    mid =0
    val =10
    high = len(elem) - 1
    number =binary_search(elem,val,low,high,mid)
    print(number)
