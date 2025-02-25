"""
There are n flights, and they are labeled from 1 to n.
We have a list of flight bookings.The i-th booking bookings[i] = [i, j, k] means that we booked k seats from flights labeled i to j inclusive.
Return an array answer of length n, representing the number of seats booked on each flight in order of their label.
"""

class Solution:
    def corpFlightBookings(self, bookings,n):
        flight_number={}
        for i in bookings:
            for j in range(len(i)):
                value =0
                value_temp = i[-1] * j
                value = value + value_temp
                flight_number[j]=value

        return flight_number

s1=Solution()

detail=s1.corpFlightBookings([[1,2,10],[2,3,20],[2,5,25]],5)
print(detail)
