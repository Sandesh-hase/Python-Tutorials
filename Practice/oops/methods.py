'''
1. Instance method
2. class method
3. static mehtod
'''

class Student:

    school = "AVCOE"
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    # Getter
    def get_m1(self ):
        return self.m1

    # Setter
    def set_m1(self,value):
        self.m1 = value

    @classmethod
    def get_school(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is the static method")

s1 = Student(34, 67, 32)
s2 = Student(89, 32, 42)

print(s1.avg())
print(s2.avg())

#setting m1 value
s1.set_m1(100)
print(s1.m1)

# Class method

print(Student.get_school())
Student.info()