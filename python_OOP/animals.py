class Animal:
    def __init__(self, name, health):
        self.name=name
        self.health=health
    def walk(self):
        self.health-=1
        return self
    def run(self):
        self.health-=5
        return self
    def displayHealth(self):
        print(self.health)

animal1=Animal('dog',10) #this works
animal1.walk().walk().walk().run().run().displayHealth() #this works 

class dog(Animal):
    def __init__(self, name, health):
        super().__init__(name,health) 
        self.health=150
    def pet(self):
        self.health+=5
        return self

phil=dog('phil',10)
phil.displayHealth()

class dragon(Animal):
    def __init__(self, name, health):
        super().__init__(name,health) # use super to call the Human __init__() method
        self.health=170
    def fly():
        self.health-=10
    def displayHealth(self):
        super().displayHealth()
        print('I am a Dragon')

dragon1=dragon('sue',50)
dragon1.displayHealth()


