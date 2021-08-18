### 3 Summ


class Threesum:

    def three_sum(self,list_num):
        output =[]
        inter =[]
        for i in range(0,len(list_num)-2):

            for j in range(i+1,len(list_num)-1):

                for k in range(j+1,len(list_num)):

                    if (list_num[i] + list_num[j] + list_num[k] == 0):
                        print(list_num[i],list_num[j],list_num[k])
                        #inter.extend([list_num[i],list_num[j],list_num[k]])


                    """
                    output.append(i)
                    output.append(j)
                    output.append(j+1)
                    """
        return inter

t1 = Threesum()
list_num =[1,0,-2,0,2,3,0,-3]
o1=t1.three_sum(list_num)
print(o1)
