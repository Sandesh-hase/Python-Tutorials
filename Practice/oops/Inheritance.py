'''
1. Single level inheritance
2. multilevel inheritance
3. Multiple inhertance
'''

class A:

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

class B:

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

class C(B):

    def feature5(self):
        print("Feature 5 working")

    def feature6(self):
        print("Feature 6 working")

# Multilevel inheritance
class D(A,B):

    def feature7(self):
        print("Feature 7 working")

    def feature8(self):
        print("Feature 8 working")



a1 = A()

a1.feature1()
a1.feature2()

b1 = B()


b1.feature4()

c1 = C()


d1 = D()

d1.feature8()

