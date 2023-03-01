
# 0 1 1 2 3 5 8 13 21 34
# Fibonacci of number less than N
N = 100

# Lets use while loop as we are not sure about the loop range
a = 0
print(a)
b = 1
print(b)
c = a + b
while c < N:
    print(c)
    a = b 
    b = c
    c = a + b
     
# Given index find fibonacci of that index

#      0 1 1 2 3 5 8 13
#index 0 1 2 3 4 5 6 7 8
# As we know the range/length of loop, will use for loop

i = 8 # Index of fibonacci
a = 0
b = 1

for x in range(i-1):
    c = a + b
    a = b
    b = c
print(f"Fibonacci at index {i} ", c)

