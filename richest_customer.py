"""

Richest Customer Wealth

"""

def maxwealth(accounts):
    #sum =0
    final_sum =[]
    for i in accounts:
        sum =0
        for j in i:
            sum = sum + j
        final_sum.append(sum)
        #print(final_sum)
        #print(sum )
    return max(final_sum)

if __name__=="__main__":
    account = [[2,8,7],[7,1,3],[1,9,5]]

    max_account = maxwealth(account)
    print(max_account)
