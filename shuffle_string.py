"""
Given a string s and an integer array indices of the same length.
The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
Input: s = "aiohn", indices = [3,1,4,2,0]
Output: "nihao"
"""

def shuffle_string(s,ind):

    str_len = len(s)
    ind_len = len(ind)

    print(str_len)
    print(ind_len)

    if str_len==ind_len:
        slist = list(s)
        final_dict ={}
        final_dict = zip(slist,ind)
    return result
if __name__=="__main__":

    s = "def"
    ind = [2,1,0]

    res = shuffle_string(s,ind)
    print(res)
