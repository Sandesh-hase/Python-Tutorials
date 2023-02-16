'''
1. Duck typing in python
2. Operator overloading
3. Method overlapping
4. Method overriding

'''
# Objects with many forms/behaviours

## Duck Typing


class PyCharm:

    def execute(self):
        print("Compiling")
        print("Runing")


class Laptop:

    def code(self,ide):
        ide.execute()

class MyEditor():

    def execute(self):
        print("Compiling")
        print("Runing")
        print("Spell Check")
        print("Chat GPT")

ide = MyEditor()

lap1 = Laptop()
lap1.code(ide)