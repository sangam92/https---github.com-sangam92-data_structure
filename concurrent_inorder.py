"""
1114. Print in Order

"""


import threading

class Foo:
    def __init__(self):
        self.val=val


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
dic={
    1:self.first,
    2:self.second,
    3:self.third
}

for i in self.val:
    
    p=threading.Thread(target=dic[i]())

    process.append(p)

for j in process:
    j.join()

