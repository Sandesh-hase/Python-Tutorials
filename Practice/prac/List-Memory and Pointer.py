a = [10,20,30]
b=a

print(a)
print(b)

a[0] = 100

print(a)
print(b)

## Two variables pointing to the same address

print(id(a))
print(id(b))

c= [100,20,30]
print(id(c))

d=list(a)  # Duplicating list with another id
print(id(d))
e = a[:]  # creates new copy of a with new address
print(id(e))

print(a is b) # Same values as well as address
print(a is c) # Same values but different address henve False

print(a==b) # Compares values and not address
print(a==c) # Compare values and not address hence True
