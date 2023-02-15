
# Self and constructor in python

class Computer:
    def __init__(self):
        self.name="Sandesh"
        self.age=25

    def update(self):
        self.age=30

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()
c2=Computer()

print(c1.name)
print(c2.name)

c1.name="Komal"
c2.age=24

print(c1.name, c1.age)
print(c2.name,c2.age)

# calling update from class to update the age

c1.update()

print(c1.name, c1.age) # Only c1 age got changes as update took c1 as a argument in via self
print(c2.name,c2.age)

# Comparing ages of two objects

if c1.compare(c2):
    print("Their age are same")
else:
    print("Their age are different")
