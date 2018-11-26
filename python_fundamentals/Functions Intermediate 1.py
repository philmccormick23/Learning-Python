# Be Cheerful
def beCheerful():
    for i in range (0,99):
        print("good monring!")
        
beCheerful()

# random integer 0-100
def randInt():
    import random
    print(int(random.random()*100))

randInt()

# random integer with max
def randInt(max=50):
    import random
    print(int(random.random()*max))

randInt()

# radom integer between 50 and 100
def randInt():
    import random
    print(int(random.uniform(50,100)))

randInt()

# random integer between 50 and 500
def randInt(max="", min=""):
    import random
    print(int(random.uniform(min,max)))

randInt(50,500)