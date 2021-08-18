"""
1436. Destination City

"""

class Solution:
    def destCity(self, paths) -> str:
        dic ={}

        for i in range(len(paths)):
            if paths[i][0] not in dic:
                dic[i]= paths[i][0]
        for j in range(len(paths)):
            
            if paths[j][1] not in dic.values():
                return paths[j][1]
            

s=Solution()

print(s.destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))