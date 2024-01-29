#1. class defination
class Add():
    #2. constructor
    def __init__(self,x,y):
        self.x=x
        self.y=y

    #3. function
    def add(self):
        print(f'{self.x+self.y}')

#2. calling
ceo1=Add(5,7)
ceo1.add()
