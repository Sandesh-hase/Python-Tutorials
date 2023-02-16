
a = 5
b = 6

print(a + b)

print(int.__add__(a,b))

c = '5'
d = '6'

print(c + d)
print(str.__add__(c,d))

## Operator overloading

class Student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)

        return s3

s1 = Student(23,23)
s2 = Student(25,25)

s3 = s1 + s2
print(s3.m1)