# MRO:- Method resolution order

class A:

    def __init__(self):
        print("In A __init__")

    def feature1(self):
        print("Feature 1-A working")

    def feature2(self):
        print("Feature 2 working")


class B:

    def __init__(self):
        print("In B __init__")

    def feature1(self):
        print("Feature 1-B working")

    def feature4(self):
        print("Feature 4 working")


class C(A,B):
    def __init__(self):
        print("In C __init__")
        super().__init__()

    def feature3(self):
        print("Feature 3-C working")

    def feature4(self):
        print("Feature 4-C working")

c1 = C()
c1.feature1() # Default it will call feature 1 of class A, as it follows the MRO,
                # so preference is always given to left one

# Same happens for constructor as well


