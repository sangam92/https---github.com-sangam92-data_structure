from collections import Counter
class Solution(object):
    def displayTable(self, orders):
        """
        :type orders: List[List[str]]
        :rtype: List[List[str]]
        """
        result=['Table']
        temp=[]
        for i in orders:
            if i[2] not in temp:
                temp.append(i[2])
        sorted_items=result+sorted(temp)
        len_sorted_items=len(sorted_items)-1
        final_result=[]
        for i in orders:
            if i[1] not in final_result:
                final_result.append(i[1])
                for j in range(0,len_sorted_items):
                    final_result.append('0')
                    
        sorted_items=[sorted_items]+[final_result]
        print(sorted_items)

        dic={}







        

    
    
s=Solution()
print(s.displayTable(orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]))


