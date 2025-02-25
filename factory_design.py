"""
Factory Design Pattern

"""

class Retail:
    def start_retail(self):
        print("The start retail has ben started")

class Hospital:
    def start_hospital(self):
        print("The hospital has been started")
class Combined:
    def start_combined(self):
        print("The combined has been created")\

class Switcher:
    

    def run(self,ip):
        if ip=='retail':
            
            Retail.start_retail()
        elif ip=='hospital':
            Hospital.start_hospital()
        else:
            return None

if __name__=="__main__":
    ip= input()
    Switcher.run(ip)