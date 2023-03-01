
num = 5429821

result = 0
while num != 0:
    last_digit = num % 10
    num = num //10
    result = result * 10
    result = result + last_digit
print(result)

