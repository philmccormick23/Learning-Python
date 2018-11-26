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
    def __init__(self, name):
        super().__init__(name, 150) 
        #self.health=150
    def random(): 
        print(10)
   

phil=dog('phil')
phil.displayHealth()
dog.random()