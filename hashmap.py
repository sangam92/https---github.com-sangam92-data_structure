"""
Design Hashmap

"""

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.load=[]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        for i in self.load:
            if key in i[0]:
                i[1]=value
            else:
                self.load.append([key,value])
                print(i[0],i[1])

        return None

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        for i in self.load:
            if key==i[0]:
                return i[1]
        return None

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        for i in self.load:
            if key==i[0]:
                del i
        return None



s=MyHashMap()

print(s.put(1,1))