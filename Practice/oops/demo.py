
class Computer:

    def config(self):
        print("This is i5, 16gb, 1TB Machine")

x=9
print(type(x))
a='8'
print(type(a))

comp1 = Computer()
print(type(comp1))

comp2 = Computer()

Computer.config(comp1)
Computer.config(comp2)

comp1.config()
comp2.config()

