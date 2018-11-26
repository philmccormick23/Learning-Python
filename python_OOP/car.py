class Car:
    tax=0
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax=.12
        if (self.price>10000):
            self.tax=.15
        
    def displayAll(self):
        print('Price: ', self.price)
        print('Speed:', self.speed)
        print('Fuel: ', self.fuel)
        print('Mileage: ', self.mileage)
        print('Tax: ', self.tax)

car1=Car(11000,50,'full',50)
car1.displayAll()

car2=Car(8000,50,'empty',50)
car2.displayAll()


    