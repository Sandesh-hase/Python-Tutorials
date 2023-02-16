

class Student:

    def __init__(self, name, rollno,):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop

    def show(self):
        print(self.name, self.rollno)

    class Laptop:
        def __init__(self):
            self.brand = "Dell"
            self.cpu = "i5"
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student("Sandesh", 10)
s2 = Student("Komal", 11)

s1.show()
s2.show()

print(s1.name, s1.rollno)

lap1 = Student.Laptop()
print("Laptop brand:- ", lap1.brand)
lap2 = s1.lap()

print("Laptop2 brand:- " ,lap2.brand)
lap1.show()
lap2.show()