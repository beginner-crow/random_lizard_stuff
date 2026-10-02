class Identity:
    def __init__(self):
        self.name = "Varkh"
        self.age = 30

class Memory:
    def __init__(self):
        self.memory = []

class Varkh:
    def __init__(self):
        self.identity = Identity()

varkh = Varkh()

print (varkh)
print ("Name's", varkh.identity.name)
print ("I am", varkh.identity.age)

print ("\nOne year later...")
varkh.identity.age += 1

print ("My birthday was a while ago, were you busy that day? Also I am now 30.")