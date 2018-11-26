class Animal:
    def __init__(self, name, health):
        self.name= name
        self.health = health
    def walk(self):
        self.health-=1
        return self
    def run(self):
        self.health-=5
        return self
    def displayHealth(self):
        print(self.health)

a1 = Animal('Rodger',15).walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    def __init__(self, name, health):
        super().__init__(name, health)
        self.health = 150
    def pet(self):
        self.health+=5
        return self

d1 =Dog('Daniel', 4).walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
    def __init__(self, name, health):
        super().__init__(name, health)
        self.health = 170
    def fly(self):
        self.health-=10
        return self
    def displayHealth(self):
        super().displayHealth()
        print('I am a Dragon')

a2  = Animal('Dave', 50)

a2.displayHealth()
