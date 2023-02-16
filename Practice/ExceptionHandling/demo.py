
a = 5
b = 0

try:

    print("Resource opened")
    print(a/b)
    print("Resource closed")
except Exception as e:
    print("Hey you can't devide number by zero!", e)

finally:
    print("Resource...closed!!")
print("Bye!")