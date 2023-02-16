a = 5

try:
    k = int(input("Enter a number:- "))
    res = a/k
    print(res)

except ValueError as e:
    print("Invalid input: " , e)

except ZeroDivisionError as e:
    print("You cant divide by zero", e)

except Exception as e:
    print("Something went wrong", e)
