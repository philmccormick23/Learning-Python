class product:
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name=item_name
        self.weight=weight
        self.brand=brand
        self.status='For Sale'

    def sell(self):
        self.status='sold'
        return self
    
    def tax(self,tax):
        self.price=self.price*(1+tax)
        return self
    
    def returnItem(self, reason):
        if(reason == 'defective'):
            self.status='defective'
            self.price=0
        if(reason=='like new'):
            self.status='For sale'
        if(reason=='opened'):
            self.status='For Sale'
            self.price=self.price*.8
        return self
        
        
    def displayInfo(self):
        print(self.price, self.item_name, self.weight, self.brand, self.status)

prod1=product(10,'toy',1,'apple')
prod1.sell().tax(.1).displayInfo()
prod1.returnItem('defective').displayInfo()
    
