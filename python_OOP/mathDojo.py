class md: 
    def __init__(self, sum):
        self.sum=0

    def add(self, *args):
        for num in args:
            self.sum+=num
        return self        

    def subtract(self, *args):
        for num in args:
            self.sum-=num
        return self
    
    def display(self):
       print(self.sum)
    
    

x = md(1)
x.add(2).add(2,5,1).subtract(3,2).display()