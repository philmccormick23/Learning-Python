class Human:
    def __init__(self):
        self.health = 5
        self.intelligence = 3
        self.strength = 2
        self.stealth = 1
    def displayHealth(self):
        print(self.health)
        return self
class Wizard(Human):
    def __init__(self):
        super().__init__() # use super to call the Human __init__() method
        self.intelligence = 10 # every wizard starts off with 10 intelligence, overwriting the 3 from Human
    def heal(self):
        self.health += 10 # all wizards also get a heal() method

phil=Wizard()
phil.displayHealth()