
result = [x**2 for x in range(1,6)]
print(result)

result = [ x for x in range(1,6)]
print(result)

result = [ [x] for x in range(1,6)]
print(result)

result = [ ["San"] for x in range(1,6)]
print(result)

result = [ [x for x in range(1,x+1)] for x in range(1,6)]
print(result)

result = [ [x for x in range(1,x+1)] for x in range(1,6) if x >2]
print(result)
