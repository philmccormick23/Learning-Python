class Bike:
    # this method to run every time a new object is instantiated
    def __init__(self, price, max_speed, miles):
	# instance attributes 
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def displayInfo(self):
        print(self.price, self.max_speed, self.miles)
        return self
    
    def ride(self):
        print('Riding')
        self.miles+=10
        return self
    
    def reverse(self):
        print('Reversing')
        if(self.miles>0):
            self.miles-=5
        return self 

bike1=Bike(200,20,0)
#bike1.ride().ride().ride().reverse().displayInfo()

bike2=Bike(200,20,0)
#bike2.ride().ride().reverse().reverse().displayInfo()

bike3=Bike(200,20,0)
bike3.reverse().reverse().reverse().displayInfo()