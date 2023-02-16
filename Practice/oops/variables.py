
class Car:

    wheels = 4  # Class variables

    def __init__(self):
        self.mil = 10  # Default value (Instance variable)
        self.com = "BMW"

c1=Car()
c2=Car()

print(c1.mil,c1.com,c1.wheels)
print(c2.mil,c2.com,c2.wheels)


# Lets change the values for whole class

c1.mil=8
Car.wheels = 3  # as it is a class variable we can change the value by calling class name
# this will be change to all the objects of that class

print(c1.mil,c1.com,c1.wheels)
print(c2.mil,c2.com,c2.wheels)

# Lets change the values for specific object

c1.mil=8
c1.wheels = 5
print(c1.mil,c1.com,c1.wheels)
print(c2.mil,c2.com,c2.wheels)