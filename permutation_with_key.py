"""
1409. Queries on a Permutation With Key

"""

class Solution:
    def processQueries(self, queries, m):
        m_list=[ i for i in range(1,m+1)]
        res=[]
        for i in queries:
           
            res.append(m_list.index(i))
            m_list.remove(i)
            m_list.insert(0,i)      
                
        return res



s=Solution()

print(s.processQueries([7,5,5,8,3],8))

        