
num = [7,8,9,5]

# print(num[1])

it = iter(num)

print(it.__next__())
print(it.__next__())
# Another way of iterating is
print(next(it))
print(next(it))
print(next(it))
