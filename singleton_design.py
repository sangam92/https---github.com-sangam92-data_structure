"""
Singleton Example
"""

class Singleton(object):
    _instance = None
    def __init__(self):
        if  self._instance is None:
           Singleton._instance=self
        else:
            raise Exception("You cannot create a singleton class") 


    def get_instance(self):
        if not Singleton._instance:
            Singleton()
        return Singleton._instance

s= Singleton()
print(s)
s1=Singleton()
print(s1)
    